import pandas as pd  # type: ignore
from scipy import stats  # type: ignore
import plotly.graph_objects as go  # type: ignore

from api.crud import (
    get_project_by_project_id,
    get_samples_by_sample_id,
    get_samples_by_sample_condition_treatment_timeline,
    get_for_subset_analysis,
)
from api.utils import analysis_html, eg_html, overview_html, subset_html


def get_projects(project_ids: list[str] | None = None) -> list[str]:
    projects = get_project_by_project_id(project_ids if project_ids else None)
    out = [proj._mapping["Project"].project_id for proj in projects]
    return out


def basic_html() -> str:
    return eg_html()


def data_overview() -> str:
    samples = get_samples_by_sample_id(None)
    data = [
        {
            "subject_id": sample._mapping["Sample"].subject_id,
            "sample_id": sample._mapping["Sample"].sample_id,
            "sample_type": sample._mapping["Sample"].sample_type,
            # "time_from_treatment_start": sample._mapping["Sample"].time_from_treatment_start,
            "b_cell": sample._mapping["Sample"].b_cell,
            "cd8_t_cell": sample._mapping["Sample"].cd8_t_cell,
            "cd4_t_cell": sample._mapping["Sample"].cd4_t_cell,
            "nk_cell": sample._mapping["Sample"].nk_cell,
            "monocyte": sample._mapping["Sample"].monocyte,
        }
        for sample in samples
    ]
    df = pd.DataFrame(data)
    df = df.sort_values(by=["sample_id"])

    cell_types = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    df["total_cells"] = df[cell_types].sum(axis=1)
    for ctype in cell_types:
        df[f"{ctype} (%)"] = ((df[ctype] / df["total_cells"]) * 100).round(2)

    df_html = df.to_html()
    return overview_html(df_html)


def statistical_analysis() -> str:
    # Get samples of type PBMC with treatment type miraclib
    samples = get_samples_by_sample_condition_treatment_timeline(
        sample_types=["PBMC"],
        conditions=["melanoma"],
        treatment_types=["miraclib"],
        time_points=None,
    )
    data = [
        {
            "subject_id": sample._mapping["Sample"].subject_id,
            "sample_id": sample._mapping["Sample"].sample_id,
            "condition": sample._mapping["Treatment"].subject_condition_name,
            "treatment": sample._mapping["Treatment"].treatment_name,
            "response": sample._mapping["Treatment"].response,
            "sample_type": sample._mapping["Sample"].sample_type,
            "time": sample._mapping["Sample"].time_from_treatment_start,
            "b_cell": sample._mapping["Sample"].b_cell,
            "cd8_t_cell": sample._mapping["Sample"].cd8_t_cell,
            "cd4_t_cell": sample._mapping["Sample"].cd4_t_cell,
            "nk_cell": sample._mapping["Sample"].nk_cell,
            "monocyte": sample._mapping["Sample"].monocyte,
        }
        for sample in samples
    ]
    df = pd.DataFrame(data)
    df = df.sort_values(by=["sample_id"])

    # Calculate cell type percentages by response status
    cell_types = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    df["total_cells"] = df[cell_types].sum(axis=1)
    for ctype in cell_types:
        df[f"{ctype} (%)"] = (df[ctype] / df["total_cells"]) * 100

    responders_df = df[df["response"]]
    non_responders_df = df[~df["response"]]

    # Perform t-tests
    stats_dict: dict = {
        "Cell Type": [],
        "Responders Mean (%)": [],
        "Non-Responders Mean (%)": [],
        "p-value": [],
    }
    for ctype in cell_types:
        _, p, *_ = stats.ttest_ind(
            responders_df[f"{ctype} (%)"],
            non_responders_df[f"{ctype} (%)"],
            equal_var=False,
        )
        stats_dict["Cell Type"].append(ctype)
        stats_dict["Responders Mean (%)"].append(
            round(responders_df[f"{ctype} (%)"].mean(), 2)
        )
        stats_dict["Non-Responders Mean (%)"].append(
            round(non_responders_df[f"{ctype} (%)"].mean(), 2)
        )
        stats_dict["p-value"].append(round(float(p), 4))  # type: ignore
    stats_df = pd.DataFrame(stats_dict)

    # Create box plots
    fig = go.Figure()
    for ctype in cell_types:
        for grp, grp_df in [
            ("Responders", responders_df),
            ("Non-Responders", non_responders_df),
        ]:
            fig.add_trace(
                go.Box(y=grp_df[f"{ctype} (%)"], name=f"{ctype} - {grp}", boxmean="sd")
            )
    fig.update_layout(
        yaxis_title="Percentage (%)",
        dragmode="pan",
        plot_bgcolor="rgb(50, 50, 50)",
        paper_bgcolor="rgb(50, 50, 50)",
        xaxis=dict(color="white", gridcolor="gray"),
        yaxis=dict(color="white", gridcolor="gray"),
        font=dict(color="white"),
    )
    config_options = {
        "displaylogo": False,
    }

    fig_html = fig.to_html(full_html=False, config=config_options)  # give a div only
    responders_df_html = responders_df.to_html()
    non_responders_df_html = non_responders_df.to_html()
    stats_df_html = stats_df.to_html()

    out = analysis_html(
        fig_html, stats_df_html, stats_df, responders_df_html, non_responders_df_html
    )

    return out


def data_subset_analysis() -> str:
    # Get samples of type PBMC with treatment type miraclib
    samples = get_for_subset_analysis(
        sample_types=["PBMC"],
        conditions=["melanoma"],
        treatment_types=["miraclib"],
        time_points=[0],
    )
    data = [
        {
            "project_id": sample._mapping["ProjectSubject"].project_id,
            "subject_id": sample._mapping["Sample"].subject_id,
            "sample_id": sample._mapping["Sample"].sample_id,
            "condition": sample._mapping["Treatment"].subject_condition_name,
            "age": sample._mapping["Subject"].age,
            "F/M": sample._mapping["Subject"].sex,
            "treatment": sample._mapping["Treatment"].treatment_name,
            "response": sample._mapping["Treatment"].response,
            "sample_type": sample._mapping["Sample"].sample_type,
            "time": sample._mapping["Sample"].time_from_treatment_start,
            "b_cell": sample._mapping["Sample"].b_cell,
            "cd8_t_cell": sample._mapping["Sample"].cd8_t_cell,
            "cd4_t_cell": sample._mapping["Sample"].cd4_t_cell,
            "nk_cell": sample._mapping["Sample"].nk_cell,
            "monocyte": sample._mapping["Sample"].monocyte,
        }
        for sample in samples
    ]
    df = pd.DataFrame(data)
    df = df.sort_values(by=["sample_id"])

    samples_per_proj_pivot = df.pivot_table(
        values=["sample_id"],
        index=["project_id"],
        aggfunc={"sample_id": pd.Series.nunique},  # type: ignore
    )
    subjects_responders_pivot = df.pivot_table(
        values=["subject_id"],
        index=["response"],
        aggfunc={"subject_id": pd.Series.nunique},  # type: ignore
    )
    subjects_sex_pivot = df.pivot_table(
        values=["subject_id"],
        index=["F/M"],
        aggfunc={"subject_id": pd.Series.nunique},  # type: ignore
    )
    big_pivot = df.pivot_table(
        values=["sample_id", "subject_id"],
        index=["project_id", "F/M", "response"],
        aggfunc={
            "sample_id": pd.Series.nunique,  # type: ignore
            "subject_id": pd.Series.nunique,  # type: ignore
        },
    )

    df_html = df.to_html()
    samples_per_proj_html = samples_per_proj_pivot.to_html()
    subjects_responders_html = subjects_responders_pivot.to_html()
    subjects_sex_html = subjects_sex_pivot.to_html()
    big_pivot_html = big_pivot.to_html()

    out = subset_html(
        samples_per_proj_html,
        subjects_responders_html,
        subjects_sex_html,
        big_pivot_html,
        df_html,
    )

    return out

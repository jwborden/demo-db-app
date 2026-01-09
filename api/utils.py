from pandas import DataFrame  # type: ignore


def analysis_html(
    fig_html: str,
    stats_df_html: str,
    stats_df: DataFrame,
    responders_df_html: str,
    non_responders_df_html: str,
) -> str:
    out = f"""
    <!doctype html>
    <html>

      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Demo - Statistical Analysis (PBMC/Melanoma/Miraclib)</title>
        <style>
          html, body {{
              width: 100%;
              margin: 0;
              padding: 0;
              background: #222;          /* dark background */
              color: #eee;               /* light text */
              font-size: 12px;          /* base font size */
          }}

          header {{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.5rem;
            margin: 20px 0;
            color: #eee;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
          }}

          h2 {{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 18px;            /* Smaller font size for h2 */
            margin: 15px 0;
            color: #eee;
            border-bottom: 1px solid #e0e0e0; /* Subtle underline */
            padding-bottom: 5px;
          }}

          p {{
            max-width: 500px;
            margin: 2rem auto;
            font-size: 14px;
            line-height: 1.5;
          }}

          nav {{
            text-align: center;
            margin: 20px 0;
            padding-top: 10px;
            padding-bottom: 20px;
          }}

          nav ul {{
            list-style: none;           /* Remove bullet points */
            padding: 0;
            margin: 0;
            display: inline-flex;       /* Horizontal layout */
            gap: 15px;                  /* Space between links */
          }}

          nav ul li {{
            display: inline;            /* Ensure list items are inline */
          }}

          nav ul li a {{
            color: #1a73e8;             /* Blue links */
            text-decoration: none;
            font-size: 1.5rem;
            padding: 10px 15px;
            border: 1px solid #1a73e8;  /* Add a border for buttons */
            border-radius: 5px;         /* Rounded corners */
            transition: all 0.3s ease;  /* Smooth hover effect */
          }}

          nav ul li a:hover {{
            background-color: #1a73e8;  /* Blue background on hover */
            color: #fff;                /* White text on hover */
          }}

          table {{
              margin: 2rem auto;          /* center the table */
              border-collapse: collapse;  /* cleaner borders */
              background: #222;           /* dark background */
              color: #fff;                /* white text */
              font-family: sans-serif;
              min-width: 300px;
          }}

          th, td {{
              padding: 0.75rem 1rem;
              border: 1px solid #444;     /* subtle borders */
              text-align: left;
          }}

          th {{
              background: #333;           /* slightly lighter header */
              font-weight: 600;
          }}

          tr:nth-child(even) td {{
              background: #2a2a2a;        /* alternating dark rows */
          }}

          tr:hover td {{
              background: #383838;        /* highlight on hover */
          }}

          .plotly-graph-div.js-plotly-plot {{
            margin: 2rem auto;
            min-height: 600px;
            max-width: 1400px;

          }}

        </style>
      </head>
      <body>
          <header>
            <h1>Demo - Statistical Analysis (PBMC/Melanoma/Miraclib)</h1>
          </header>
          <nav>
            <ul>
              <li><a href="#cell-type-percentages">Cell Type Percentages by Response Status</a></li>
              <li><a href="#t-test-comparison">T-test Comparison</a></li>
              <li><a href="#responders-data">Responders Data</a></li>
              <li><a href="#non-responders-data">Non-Responders Data</a></li>
            </ul>
          </nav>
          <main>
            <section id="cell-type-percentages"">
              <h2>Cell Type Percentages by Response Status (PBMC/Melanoma/Miraclib)</h2>
              {fig_html}
            </section>
            <section id="t-test-comparison">
              <h2>T-test Comparison (PBMC/Melanoma/Miraclib)</h2>
              {stats_df_html}
              <p>
                CD4 T-cells show a statistically significant difference in relative
                frequencies between responders and non-responders (p &lt; 0.05),
                however, the means are quite close (Responders: {stats_df.loc[stats_df["Cell Type"] == "cd4_t_cell", "Responders Mean (%)"].values[0]}%,
                Non-Responders: {stats_df.loc[stats_df["Cell Type"] == "cd4_t_cell", "Non-Responders Mean (%)"].values[0]}%), suggesting
                that the effect size may not be clinically significant.
              </p>
            </section>
            <section id="responders-data">
              <h2>Responders Data (PBMC/Melanoma/Miraclib)</h2>
              {responders_df_html}
            </section>
            <section id="non-responders-data">
              <h2>Non-Responders Data (PBMC/Melanoma/Miraclib)</h2>
              {non_responders_df_html}
            </section>
          </main>
      </body>
    </html>
    """

    return out


def eg_html() -> str:
    out = """
    <html>
      <head>
        <title>Demo</title>
      </head>
      <body>
        <h1>Demo Service</h1>
        <p>This is a basic HTML response from the Demo Service.</p>
      </body>
    </html>
    """
    return out


def overview_html(df_html: str) -> str:
    out = f"""
    <!doctype html>
    <html>

      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Demo - Data Overview</title>
        <style>
          html, body {{
              width: 100%;
              margin: 0;
              padding: 0;
              background: #222;          /* dark background */
              color: #eee;               /* light text */
              font-size: 12px;          /* base font size */
          }}

          header {{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.5rem;
            margin: 20px 0;
            color: #eee;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
          }}

          table {{
              margin: 2rem auto;          /* center the table */
              border-collapse: collapse;  /* cleaner borders */
              background: #222;           /* dark background */
              color: #fff;                /* white text */
              font-family: sans-serif;
              min-width: 300px;
          }}

          th, td {{
              padding: 0.75rem 1rem;
              border: 1px solid #444;     /* subtle borders */
              text-align: left;
          }}

          th {{
              background: #333;           /* slightly lighter header */
              font-weight: 600;
          }}

          tr:nth-child(even) td {{
              background: #2a2a2a;        /* alternating dark rows */
          }}

          tr:hover td {{
              background: #383838;        /* highlight on hover */
          }}
        </style>
      </head>
      <body>
          <header>
            <h1>Demo - Data Overview</h1>
          </header>
          <main>
            <section>
              {df_html}
            </section>
          </main>
      </body>
    </html>
    """

    return out


def subset_html(
    samples_per_proj_html: str,
    subjects_responders_html: str,
    subjects_sex_html: str,
    big_pivot_html: str,
    df_html: str,
) -> str:
    out = f"""
    <!doctype html>
    <html>

      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Demo - Data Subset Analysis (PBMC/Melanoma/Miraclib/Baseline)</title>
        <style>
          html, body {{
              width: 100%;
              margin: 0;
              padding: 0;
              background: #222;          /* dark background */
              color: #eee;               /* light text */
              font-size: 12px;          /* base font size */
          }}

          header {{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.5rem;
            margin: 20px 0;
            color: #eee;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
          }}

          h2 {{
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 18px;            /* Smaller font size for h2 */
            margin: 15px 0;
            color: #eee;
            border-bottom: 1px solid #e0e0e0; /* Subtle underline */
            padding-bottom: 5px;
          }}

          p {{
            max-width: 500px;
            margin: 2rem auto;
            font-size: 14px;
            line-height: 1.5;
          }}

          nav {{
            text-align: center;
            margin: 20px 0;
            padding-top: 10px;
            padding-bottom: 20px;
          }}

          nav ul {{
            list-style: none;           /* Remove bullet points */
            padding: 0;
            margin: 0;
            display: inline-flex;       /* Horizontal layout */
            gap: 15px;                  /* Space between links */
          }}

          nav ul li {{
            display: inline;            /* Ensure list items are inline */
          }}

          nav ul li a {{
            color: #1a73e8;             /* Blue links */
            text-decoration: none;
            font-size: 1.5rem;
            padding: 10px 15px;
            border: 1px solid #1a73e8;  /* Add a border for buttons */
            border-radius: 5px;         /* Rounded corners */
            transition: all 0.3s ease;  /* Smooth hover effect */
          }}

          nav ul li a:hover {{
            background-color: #1a73e8;  /* Blue background on hover */
            color: #fff;                /* White text on hover */
          }}

          table {{
              margin: 2rem auto;          /* center the table */
              border-collapse: collapse;  /* cleaner borders */
              background: #222;           /* dark background */
              color: #fff;                /* white text */
              font-family: sans-serif;
              min-width: 300px;
          }}

          th, td {{
              padding: 0.75rem 1rem;
              border: 1px solid #444;     /* subtle borders */
              text-align: left;
          }}

          th {{
              background: #333;           /* slightly lighter header */
              font-weight: 600;
          }}

          tr:nth-child(even) td {{
              background: #2a2a2a;        /* alternating dark rows */
          }}

          tr:hover td {{
              background: #383838;        /* highlight on hover */
          }}

          .plotly-graph-div.js-plotly-plot {{
            margin: 2rem auto;
            min-height: 600px;
            max-width: 1400px;

          }}

        </style>
      </head>
      <body>
          <header>
            <h1>Demo - Data Subset Analysis (PBMC/Melanoma/Miraclib/Baseline)</h1>
          </header>
          <nav>
            <ul>
              <li><a href="#samples-per-project">Samples Per Project</a></li>
              <li><a href="#responders-vs-non-responders">Responders (True) vs. Non-Responders (False)</a></li>
              <li><a href="#patient-sex-distribution">Patient Sex Distribution</a></li>
              <li><a href="#subset-analysis-summary">Subset Analysis Summary</a></li>
              <li><a href="#all-patient-samples">All Patient Samples</a></li>
            </ul>
          </nav>
          <main>
            <section id="samples-per-project">
              <h2>Samples Per Project (PBMC/Melanoma/Miraclib/Baseline)</h2>
              {samples_per_proj_html}
            </section>
            <section id="responders-vs-non-responders">
              <h2>Responders (True) vs. Non-Responders (False) (PBMC/Melanoma/Miraclib/Baseline)</h2>
              {subjects_responders_html}
            </section>
            <section id="patient-sex-distribution">
              <h2>Patient Sex Distribution (PBMC/Melanoma/Miraclib/Baseline)</h2>
              {subjects_sex_html}
            </section>
            <section id="subset-analysis-summary">
              <h2>Subset Analysis Summary (PBMC/Melanoma/Miraclib/Baseline)</h2>
              {big_pivot_html}
            </section>
            <section id="all-patient-samples">
              <h2>All Patient Samples (PBMC/Melanoma/Miraclib/Baseline)</h2>
              {df_html}
            </section>
          </main>
      </body>
    </html>
    """

    return out

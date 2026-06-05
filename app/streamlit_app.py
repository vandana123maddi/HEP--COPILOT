import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import streamlit as st
import plotly.express as px

from analysis.router import route_query
from analysis.copilot import generate_response

st.set_page_config(
    page_title="HEP Copilot",
    layout="wide"
)

st.title("HEP Copilot")

query = st.text_input(
    "Ask a High Energy Physics question"
)

if st.button("Run"):

    result = route_query(query)

    if isinstance(result, dict):

        if "error" in result:
            st.error(
                result["error"]
            )

        st.subheader(
            result["analysis"]
        )

        with st.spinner(
            "Asking Gemini..."
        ):

            explanation = generate_response(
                query,
                result
            )

        st.info(
            explanation
        )

        if "events_processed" in result:

            st.metric(
                "Events Processed",
                result["events_processed"]
            )

        if "mean_mass" in result:

            st.metric(
                "Mean Mass (GeV)",
                round(
                    result["mean_mass"],
                    2
                )
            )

        if "max_mass" in result:

            st.metric(
                "Maximum Mass (GeV)",
                round(
                    result["max_mass"],
                    2
                )
            )

        if "min_mass" in result:

            st.metric(
                "Minimum Mass (GeV)",
                round(
                    result["min_mass"],
                    2
                )
            )

        if "sample_masses" in result:

            fig = px.histogram(
                x=result["sample_masses"],
                nbins=50,
                title="CMS Open Data Dimuon Mass Spectrum"
            )

            fig.update_xaxes(
                title="Dimuon Mass (GeV)"
            )

            fig.update_yaxes(
                title="Events"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        if "sample_pts" in result:

            fig = px.histogram(
                x=result["sample_pts"],
                nbins=50,
                title="CMS pT Distribution"
            )

            fig.update_xaxes(
                title="Transverse Momentum (GeV)"
            )

            fig.update_yaxes(
                title="Events"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            generate_response(
                query,
                None
            )
        )


from pathlib import Path

import gradio as gr

from summarizer import summarize


# Load the external CSS file
BASE_DIR = Path(__file__).resolve().parent
CSS_PATH = BASE_DIR / "static" / "style.css"
CUSTOM_CSS = CSS_PATH.read_text(encoding="utf-8")


def summarize_website(url):
    """Validate the URL and generate a website summary."""
    if not url or not url.strip():
        raise gr.Error("Please enter a website URL.")

    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        result = summarize(url)

        if not result:
            raise gr.Error("The AI returned an empty summary. Please try again.")

        return result

    except gr.Error:
        raise

    except Exception as error:
        print(f"Summarization error: {error}")
        raise gr.Error(
            "Could not summarize this website. "
            "Please check the URL and try again."
        ) from error


with gr.Blocks(
    css=CUSTOM_CSS,
    title="AI Website Summarizer",
    theme=gr.themes.Base(
        primary_hue="blue",
        neutral_hue="slate",
    ),
) as app:

    # Header
    with gr.Column(elem_classes=["main-container"]):

        with gr.Row(elem_classes=["hero-section"]):
            with gr.Column(elem_classes=["hero-content"]):
                gr.Markdown(
                    """
                    <div class="brand-label">
                        <span class="brand-icon">✦</span>
                        AI POWERED TOOL
                    </div>

                    <h1 class="hero-title">
                        AI Website <span>Summarizer</span>
                    </h1>

                    <p class="hero-description">
                        Turn lengthy websites into clear, concise summaries.
                        Get the main ideas without reading every word.
                    </p>
                    """,
                    elem_classes=["header-markdown"],
                )

        # URL input section
        with gr.Column(elem_classes=["input-card"]):
            gr.Markdown(
                """
                <div class="section-heading">
                    <span class="section-number">01</span>
                    <div>
                        <h2>Enter a website</h2>
                        <p>Paste the URL of the page you want to understand.</p>
                    </div>
                </div>
                """
            )

            website_url = gr.Textbox(
                label="Website URL",
                placeholder="https://example.com",
                lines=1,
                max_lines=1,
                elem_id="website-url",
            )

            with gr.Row(elem_classes=["action-row"]):
                summarize_button = gr.Button(
                    "✦  Summarize Website",
                    variant="primary",
                    elem_id="summarize-button",
                    scale=4,
                )

                clear_button = gr.Button(
                    "Clear",
                    variant="secondary",
                    elem_id="clear-button",
                    scale=1,
                )

            gr.Markdown(
                """
                <p class="privacy-note">
                    <span>●</span>
                    Your URL is processed when you click Summarize.
                </p>
                """
            )

        # Summary output section
        with gr.Column(elem_classes=["output-card"]):
            with gr.Row(elem_classes=["output-heading"]):
                gr.Markdown(
                    """
                    <div class="section-heading">
                        <span class="section-number">02</span>
                        <div>
                            <h2>Your summary</h2>
                            <p>Key information, organized for easy reading.</p>
                        </div>
                    </div>
                    """
                )

                status = gr.Markdown(
                    '<span class="status-badge">READY</span>',
                    elem_id="summary-status",
                )

            summary_output = gr.Markdown(
                value=(
                    "### Your summary will appear here\n\n"
                    "Enter a website URL above and click "
                    "**Summarize Website** to get started."
                ),
                elem_id="summary-output",
            )

        # Footer
        gr.Markdown(
            """
            <div class="app-footer">
                <span>AI Website Summarizer</span>
                <span>Built with Python · Gradio · Groq</span>
            </div>
            """,
            elem_classes=["footer-markdown"],
        )

    # Connect the UI to the existing summarizer function
    summarize_button.click(
        fn=summarize_website,
        inputs=website_url,
        outputs=summary_output,
        show_progress="full",
    ).then(
        fn=lambda: '<span class="status-badge">COMPLETED</span>',
        inputs=None,
        outputs=status,
    )

    # Clear the input and restore the initial output
    clear_button.click(
        fn=lambda: (
            "",
            "### Your summary will appear here\n\n"
            "Enter a website URL above and click "
            "**Summarize Website** to get started.",
            '<span class="status-badge">READY</span>',
        ),
        inputs=None,
        outputs=[website_url, summary_output, status],
    )


if __name__ == "__main__":
    app.launch()

from flask import Flask, render_template, request, send_file
from PIL import Image
from pdf2image import convert_from_path
import pypandoc
import os

app = Flask(__name__)

# Folders for uploads and outputs
UPLOAD_FOLDER = "admin/input"
OUTPUT_FOLDER = "admin/output"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]
    conversion_type = request.form["conversion_type"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)
    output_path = os.path.join(OUTPUT_FOLDER, "converted_output")

    try:
        # --- Image to PDF ---
        if conversion_type == "jpg_to_pdf" or conversion_type == "png_to_pdf":
            image = Image.open(input_path).convert("RGB")
            output_file = f"{output_path}.pdf"
            image.save(output_file)

        # --- PDF to Image ---
        elif conversion_type == "pdf_to_jpg":
            pages = convert_from_path(input_path)
            output_file = f"{output_path}.jpg"
            pages[0].save(output_file, "JPEG")

        # --- Word & PPT Conversions ---
        elif conversion_type == "word_to_pdf":
            output_file = f"{output_path}.pdf"
            pypandoc.convert_file(input_path, "pdf", outputfile=output_file)

        elif conversion_type == "pdf_to_word":
            output_file = f"{output_path}.docx"
            pypandoc.convert_file(input_path, "docx", outputfile=output_file)

        elif conversion_type == "ppt_to_pdf":
            output_file = f"{output_path}.pdf"
            pypandoc.convert_file(input_path, "pdf", outputfile=output_file)

        elif conversion_type == "pdf_to_ppt":
            output_file = f"{output_path}.pptx"
            pypandoc.convert_file(input_path, "pptx", outputfile=output_file)

        else:
            return "Invalid conversion type"

        # Redirect to download page
        filename = os.path.basename(output_file)
        return render_template("Ktwo.html", file_name=filename)

    except Exception as e:
        return f"Error during conversion: {str(e)}"

@app.route("/download/<file_name>")
def download(file_name):
    file_path = os.path.join(OUTPUT_FOLDER, file_name)
    return send_file(file_path, as_attachment=True)

@app.route("/clear", methods=["POST"])
def clear_files():
    try:
        for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        return "✅ All files cleared successfully!"
    except Exception as e:
        return f"Error clearing files: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, render_template, request, send_file
from PIL import Image
from pdf2image import convert_from_path
import pypandoc
import os

app = Flask(__name__)

# Folders for uploads and outputs
UPLOAD_FOLDER = "admin/input"
OUTPUT_FOLDER = "admin/output"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]
    conversion_type = request.form["conversion_type"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)
    output_path = os.path.join(OUTPUT_FOLDER, "converted_output")

    try:
        # --- Image to PDF ---
        if conversion_type == "jpg_to_pdf" or conversion_type == "png_to_pdf":
            image = Image.open(input_path).convert("RGB")
            output_file = f"{output_path}.pdf"
            image.save(output_file)

        # --- PDF to Image ---
        elif conversion_type == "pdf_to_jpg":
            pages = convert_from_path(input_path)
            output_file = f"{output_path}.jpg"
            pages[0].save(output_file, "JPEG")

        # --- Word & PPT Conversions ---
        elif conversion_type == "word_to_pdf":
            output_file = f"{output_path}.pdf"
            pypandoc.convert_file(input_path, "pdf", outputfile=output_file)

        elif conversion_type == "pdf_to_word":
            output_file = f"{output_path}.docx"
            pypandoc.convert_file(input_path, "docx", outputfile=output_file)

        elif conversion_type == "ppt_to_pdf":
            output_file = f"{output_path}.pdf"
            pypandoc.convert_file(input_path, "pdf", outputfile=output_file)

        elif conversion_type == "pdf_to_ppt":
            output_file = f"{output_path}.pptx"
            pypandoc.convert_file(input_path, "pptx", outputfile=output_file)

        else:
            return "Invalid conversion type"

        # Redirect to download page
        filename = os.path.basename(output_file)
        return render_template("Ktwo.html", file_name=filename)

    except Exception as e:
        return f"Error during conversion: {str(e)}"

@app.route("/download/<file_name>")
def download(file_name):
    file_path = os.path.join(OUTPUT_FOLDER, file_name)
    return send_file(file_path, as_attachment=True)

@app.route("/clear", methods=["POST"])
def clear_files():
    try:
        for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        return "✅ All files cleared successfully!"
    except Exception as e:
        return f"Error clearing files: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


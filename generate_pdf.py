import os
import subprocess
import qrcode
import base64
from io import BytesIO

# ============================================================
# STEP 1: Real QR Code generate karo (base64 mein)
# ============================================================
qr = qrcode.QRCode(version=2, box_size=5, border=2)
qr.add_data("https://ptu.ac.in/result/2130733")
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
buffered = BytesIO()
qr_img.save(buffered, format="PNG")
qr_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
qr_data_url = f"data:image/png;base64,{qr_base64}"

# Logo path
logo_path = r"C:/Users/Ravi Rai/.gemini/antigravity/brain/892936bc-2cec-4802-8887-c5c798355c74/.user_uploaded/media_1790760778960.png"

# ============================================================
# STEP 2: HTML Template - ekdum original jaise
# ============================================================
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Grade Sheet - Ravi Rai</title>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
        font-family: Arial, sans-serif;
        padding: 22px 38px;
        color: #000;
        font-size: 12.5px;
    }}

    /* ---- HEADER ---- */
    .header {{
        text-align: center;
        position: relative;
        margin-bottom: 8px;
    }}
    .punjabi-text {{
        font-size: 21px;
        font-family: "Raavi", "Noto Serif Gurmukhi", "Noto Sans Gurmukhi", serif;
        margin-bottom: 3px;
        letter-spacing: 0.5px;
    }}
    .university-name {{
        font-size: 26px;
        font-family: "Old English Text MT", "Engravers Old English BT", serif;
        margin-bottom: 2px;
    }}
    .formerly {{
        font-size: 10px;
        margin-bottom: 1px;
    }}
    .old-university-name {{
        font-size: 19px;
        font-family: "Old English Text MT", "Engravers Old English BT", serif;
    }}
    .edp-no {{
        position: absolute;
        top: 0;
        right: 0;
        font-size: 11px;
        text-align: right;
        line-height: 1.5;
    }}

    /* ---- TOP INFO ROW ---- */
    .top-info {{
        position: relative;
        width: 100%;
        height: 110px;
        margin-top: 10px;
        margin-bottom: 12px;
    }}
    .student-details-left {{
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        font-size: 12.5px;
        line-height: 1.6;
    }}
    .student-details-left .roll {{
        font-weight: bold;
    }}
    .student-details-left .college-label {{
        color: #000;
    }}
    .student-details-left .college-name {{
        font-weight: bold;
        color: #000;
    }}
    .logo-container {{
        position: absolute;
        left: 50%;
        top: 35%;
        transform: translate(-50%, -50%);
    }}
    .logo-container img {{
        width: 90px;
        height: 90px;
        object-fit: contain;
    }}
    .qr-container {{
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
    }}
    .qr-container img {{
        width: 95px;
        height: 95px;
    }}

    /* ---- GRADE SHEET TITLE ---- */
    .sheet-title {{
        text-align: center;
        margin-bottom: 8px;
    }}
    .sheet-title h2 {{
        font-family: "Brush Script MT", "Brush Script Std", "Lucida Calligraphy", cursive;
        font-size: 29px;
        font-weight: normal;
        font-style: italic;
        margin-bottom: 4px;
        color: #1e293b;
    }}
    .sheet-subtitle {{
        font-size: 12.5px;
        font-weight: bold;
        color: #000;
    }}

    /* ---- PERSONAL INFO ---- */
    .personal-info {{
        margin-bottom: 10px;
    }}
    .personal-info table {{
        border-collapse: collapse;
    }}
    .personal-info table td {{
        padding: 1px 0;
        font-size: 12.5px;
    }}
    .personal-info table td:first-child {{
        width: 100px;
        font-weight: normal;
    }}
    .personal-info table td:nth-child(2) {{
        width: 15px;
        text-align: left;
    }}

    /* ---- GRADES TABLE ---- */
    .grades-table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 8px;
        font-size: 12px;
    }}
    .grades-table th, .grades-table td {{
        border: 1px solid #000;
        padding: 3px 5px;
        text-align: center;
    }}
    .grades-table th:nth-child(1), .grades-table td:nth-child(1) {{
        width: 72px;
        word-break: break-all;
    }}
    .grades-table td:nth-child(2) {{
        text-align: left;
        padding-left: 8px;
    }}
    .grades-table th:nth-child(3), .grades-table td:nth-child(3) {{
        width: 75px;
    }}
    .grades-table th:nth-child(4), .grades-table td:nth-child(4) {{
        width: 60px;
    }}
    .grades-table th:nth-child(5), .grades-table td:nth-child(5) {{
        width: 55px;
    }}

    /* ---- SUMMARY ---- */
    .summary-info {{
        display: flex;
        justify-content: space-between;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 12.5px;
    }}

    /* ---- BOTTOM ---- */
    .bottom-left {{ line-height: 1.8; font-size: 12.5px; }}
    .bottom-left span {{ display: inline-block; width: 170px; font-weight: bold; }}

    .edp-cell {{ font-weight: bold; margin-top: 10px; margin-bottom: 8px; }}

    .signatures {{
        display: flex;
        justify-content: space-between;
        text-align: center;
        font-size: 11px;
        font-weight: bold;
    }}
    .signature-box {{ width: 22%; }}
    .sig-line {{ margin-top: 22px; padding-top: 4px; }}
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
    <div class="punjabi-text">ਆਈ.ਕੇ.ਗੁਜਰਾਲ ਪੰਜਾਬ ਟੈਕਨੀਕਲ ਯੂਨੀਵਰਸਿਟੀ</div>
    <div class="university-name">I.K.Gujral Punjab Technical University</div>
    <div class="formerly">Formerly</div>
    <div class="old-university-name">Punjab Technical University</div>
    <div class="edp-no">S.No. of EDP<br><strong>1002785552</strong></div>
</div>

<!-- TOP ROW: Student info | Logo | QR -->
<div class="top-info">
    <div class="student-details-left">
        Regn. cum Roll No: &nbsp;<span class="roll">2130733</span><br>
        <span class="college-label">Name of the College/Institute:</span><br>
        <span class="college-name">Gulzar Group of Institutes, Khanna,<br>Ludhiana</span>
    </div>
    <div class="logo-container">
        <img src="file:///{logo_path.replace(chr(92), '/')}" alt="PTU Logo">
    </div>
    <div class="qr-container">
        <img src="{qr_data_url}" alt="QR Code">
    </div>
</div>

<!-- GRADE SHEET TITLE -->
<div class="sheet-title">
    <h2><u>Grade Sheet</u></h2>
    <div class="sheet-subtitle">Bachelor of Technology (Computer Science &amp; Engineering),FOURTH Semester,April-2025</div>
</div>

<!-- PERSONAL INFO -->
<div class="personal-info">
    <table>
        <tr><td>Name</td><td>:</td><td><strong>RAVI RAI</strong></td></tr>
        <tr><td>Father's Name</td><td>:</td><td><strong>UMESH RAI</strong></td></tr>
        <tr><td>Mother's Name</td><td>:</td><td><strong>ANJU DEVI</strong></td></tr>
    </table>
</div>

<!-- GRADES TABLE -->
<table class="grades-table">
    <tr><th>Subject<br>Code</th><th>Subject</th><th>Type</th><th>Credits</th><th>Grade</th></tr>
    <tr><td>BTCS-401-18</td><td>Discrete Mathematics</td><td>Theory</td><td>4</td><td>P</td></tr>
    <tr><td>BTCS-402-18</td><td>Operating Systems</td><td>Theory</td><td>3</td><td>B</td></tr>
    <tr><td>BTCS-403-18</td><td>Design &amp; Analysis of Algorithms</td><td>Theory</td><td>3</td><td>B+</td></tr>
    <tr><td>BTCS-404-18</td><td>Operating Systems Lab</td><td>Practical</td><td>2</td><td>A</td></tr>
    <tr><td>BTCS-405-18</td><td>Design &amp; Analysis of Algorithms Lab</td><td>Practical</td><td>2</td><td>A</td></tr>
    <tr><td>BTES-401-18</td><td>Computer Organization &amp; Architecture</td><td>Theory</td><td>3</td><td>B</td></tr>
    <tr><td>BTES-402-18</td><td>Computer Organization &amp; Architecture Lab</td><td>Practical</td><td>1</td><td>A+</td></tr>
    <tr><td>EVS 101-18</td><td>Environmental Sciences</td><td>Practical</td><td>0</td><td>A+</td></tr>
    <tr><td>HSMC-122-18</td><td>Universal Human Values</td><td>Theory</td><td>3</td><td>B</td></tr>
</table>

<!-- SUMMARY -->
<div class="summary-info">
    <div>Credits Registered in the Semester :21</div>
    <div>Semester Grade Point Average (SGPA) : 6.29</div>
</div>

<!-- BOTTOM INFO -->
<div class="bottom-left">
    <div><span>Notification Result Date</span> : &nbsp;<strong>01.08.2025</strong></div>
    <div><span>Place</span> : &nbsp;<strong>JALANDHAR</strong></div>
    <div><span>Date of Issue</span> : &nbsp;<strong>01.08.2025</strong></div>
</div>

<div class="edp-cell">E.D.P. CELL</div>

<div class="signatures">
    <div class="signature-box"><div class="sig-line">Prepared By</div></div>
    <div class="signature-box">
        <img src="file:///C:/Users/Ravi Rai/.gemini/antigravity/scratch/sig2_checked.png" style="height:40px; display:block; margin: 0 auto 2px auto;">
        <div class="sig-line">Checked &amp; Verified By</div>
    </div>
    <div class="signature-box">
        <img src="file:///C:/Users/Ravi Rai/.gemini/antigravity/scratch/sig2_officer.png" style="height:40px; display:block; margin: 0 auto 2px auto;">
        <div class="sig-line">Officer Incharge</div>
    </div>
    <div class="signature-box">
        <img src="file:///C:/Users/Ravi Rai/.gemini/antigravity/scratch/sig2_controller.png" style="height:40px; display:block; margin: 0 auto 2px auto;">
        <div class="sig-line">Controller of Examinations</div>
    </div>
</div>

</body>
</html>"""

# ============================================================
# STEP 3: Save HTML & Convert to PDF
# ============================================================
html_path = os.path.join(os.getcwd(), "temp_gradesheet_v2.html")
pdf_path  = os.path.join(os.getcwd(), "Final_Grade_Sheet_v2.pdf")

print("1. Creating HTML...")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("2. Converting to PDF via Edge...")
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = f'"{edge_path}" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="{pdf_path}" "file:///{html_path.replace(chr(92), "/")}"'
subprocess.run(cmd, shell=True)

print(f"\nDONE! PDF saved at:\n{pdf_path}")

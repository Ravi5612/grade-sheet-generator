import os
work_dir = r'C:/Users/Ravi Rai/.gemini/antigravity/scratch/grade-sheet-generator'
import base64

def to_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

logo_b64 = to_b64(os.path.join(work_dir, 'ptu_logo.png'))
sig_checked_b64 = to_b64(os.path.join(work_dir, 'sig_checked.png'))
sig_officer_b64 = to_b64(os.path.join(work_dir, 'sig_officer.png'))
sig_ctrl_b64 = to_b64(os.path.join(work_dir, 'sig_controller.png'))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PTU Grade Sheet</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: Arial, sans-serif; background: #fff; }}

  /* Top navbar */
  .navbar {{ background-color: #8B0000; color: white; padding: 10px 20px; font-size: 15px; font-weight: bold; letter-spacing: 0.5px; }}
  @media print {{ .navbar {{ display: none !important; }} }}

  .container {{ max-width: 820px; margin: 30px auto; background: white; padding: 30px 45px; }}

  /* HEADER */
  .header {{ text-align: center; position: relative; margin-bottom: 18px; }}
  .punjabi-text {{ font-size: 22px; font-family: "Raavi", "Noto Serif Gurmukhi", serif; margin-bottom: 4px; }}
  .university-name {{ font-size: 28px; font-family: "Old English Text MT", "Engravers Old English BT", serif; margin-bottom: 3px; }}
  .formerly {{ font-size: 11px; margin-bottom: 2px; color: #444; }}
  .old-university-name {{ font-size: 20px; font-family: "Old English Text MT", "Engravers Old English BT", serif; }}
  .edp-no {{ position: absolute; top: 0; right: 0; font-size: 11px; text-align: right; line-height: 1.7; }}

  /* TOP INFO ROW */
  .top-info {{ position: relative; width: 100%; height: 120px; margin: 15px 0 18px 0; }}
  .student-details-left {{ position: absolute; left: 0; top: 50%; transform: translateY(-50%); font-size: 13px; line-height: 1.75; }}
  .student-details-left .roll {{ font-weight: bold; }}
  .student-details-left .college-name {{ font-weight: bold; }}
  .logo-container {{ position: absolute; left: 50%; top: 40%; transform: translate(-50%, -50%); text-align: center; }}
  .logo-container img {{ width: 95px; height: 95px; object-fit: contain; }}
  .qr-container {{ position: absolute; right: 0; top: 50%; transform: translateY(-50%); width: 100px; height: 100px; }}
  
  #qrcode img {{ width: 100%; height: 100%; image-rendering: pixelated; display: block; margin: auto; }}
  #qrcode img, #qrcode canvas {{ width: 100% !important; height: 100% !important; display: block; margin: auto; }}
  /* GRADE SHEET TITLE */
  .sheet-title {{ text-align: center; margin-bottom: 10px; }}
  .sheet-title h2 {{ font-family: "Brush Script MT", cursive; font-size: 32px; font-weight: normal; font-style: italic; color: #1e293b; margin-bottom: 5px; }}
  .sheet-subtitle {{ font-size: 13px; font-weight: bold; }}

  /* PERSONAL INFO */
  .personal-info {{ margin-bottom: 12px; }}
  .personal-info table td {{ padding: 2px 0; font-size: 13px; }}
  .personal-info table td:first-child {{ width: 105px; }}
  .personal-info table td:nth-child(2) {{ width: 15px; }}

  /* GRADES TABLE */
  .grades-table {{ width: 100%; border-collapse: collapse; margin-bottom: 10px; font-size: 13px; }}
  .grades-table th, .grades-table td {{ border: 1px solid #000; padding: 5px 6px; text-align: center; }}
  .grades-table th:nth-child(1), .grades-table td:nth-child(1) {{ width: 72px; word-break: break-all; }}
  .grades-table td:nth-child(2) {{ text-align: left; padding-left: 8px; }}
  .grades-table th:nth-child(3), .grades-table td:nth-child(3) {{ width: 80px; }}
  .grades-table th:nth-child(4), .grades-table td:nth-child(4) {{ width: 65px; }}
  .grades-table th:nth-child(5), .grades-table td:nth-child(5) {{ width: 60px; }}

  /* SUMMARY */
  .summary-info {{ display: flex; justify-content: space-between; font-weight: bold; font-size: 13px; margin-bottom: 10px; }}

  /* BOTTOM INFO */
  .bottom-left {{ font-size: 13px; line-height: 1.9; }}
  .bottom-left span {{ display: inline-block; width: 175px; font-weight: bold; }}

  .edp-cell {{ font-weight: bold; margin-top: 12px; margin-bottom: 10px; font-size: 13px; }}

  /* SIGNATURES */
  .signatures {{ display: flex; justify-content: space-between; text-align: center; font-size: 11.5px; font-weight: bold; margin-top: 8px; }}
  .signature-box {{ width: 23%; }}
  .sig-img {{ height: 42px; margin-bottom: 3px; display:block; margin-left:auto; margin-right:auto; }}

  /* Print button */
  .print-btn {{ display: block; margin: 20px auto 0 auto; padding: 10px 30px; background: #8B0000; color: white; border: none; font-size: 14px; cursor: pointer; border-radius: 4px; font-weight: bold; text-align:center; text-decoration:none; width: 200px; }}
  .print-btn:hover {{ background: #a00000; }}
  @media print {{ .print-btn {{ display: none !important; }} .container {{ margin: 0; box-shadow: none; padding: 0; }} }}

  /* ---- MOBILE RESPONSIVE ---- */
  @media (max-width: 640px) {{
    .container {{ padding: 15px 12px; margin: 10px auto; }}

    /* Header */
    .punjabi-text {{ font-size: 16px; padding-right: 60px; }}
    .university-name {{ font-size: 19px; }}
    .old-university-name {{ font-size: 15px; }}
    .edp-no {{ font-size: 10px; }}

    /* Top info - switch from absolute to flex layout on mobile */
    .top-info {{ position: static; height: auto; display: flex; flex-direction: column; align-items: flex-start; gap: 10px; margin: 10px 0; }}
    .student-details-left {{ position: static; transform: none; font-size: 12px; line-height: 1.6; }}
    .logo-container {{ position: static; transform: none; display: none; }}
    .qr-container {{ position: static; transform: none; width: 80px; height: 80px; align-self: flex-end; margin-top: -60px; }}
    .qr-container img {{ width: 80px; height: 80px; }}

    /* Title */
    .sheet-title h2 {{ font-size: 24px; }}
    .sheet-subtitle {{ font-size: 11px; }}

    /* Personal info */
    .personal-info table td {{ font-size: 11px; }}
    .personal-info table td:first-child {{ width: 85px; }}

    /* Grades table */
    .grades-table {{ font-size: 10px; }}
    .grades-table th, .grades-table td {{ padding: 3px 3px; }}
    .grades-table th:nth-child(1), .grades-table td:nth-child(1) {{ width: 55px; }}
    .grades-table th:nth-child(3), .grades-table td:nth-child(3) {{ width: 55px; }}
    .grades-table th:nth-child(4), .grades-table td:nth-child(4) {{ width: 45px; }}
    .grades-table th:nth-child(5), .grades-table td:nth-child(5) {{ width: 38px; }}

    /* Summary */
    .summary-info {{ flex-direction: column; font-size: 11px; gap: 4px; }}

    /* Bottom */
    .bottom-left {{ font-size: 11px; }}
    .bottom-left span {{ width: 140px; }}

    /* Signatures */
    .signatures {{ font-size: 9.5px; }}
    .sig-img {{ height: 32px; }}
    .signature-box {{ width: 24%; }}
  }}
</style>
</head>
<body>

<div class="navbar">Online Degree/DMC Verification</div>

<div class="container">
  <div class="header">
    <div class="punjabi-text">ਆਈ.ਕੇ.ਗੁਜਰਾਲ ਪੰਜਾਬ ਟੈਕਨੀਕਲ ਯੂਨੀਵਰਸਿਟੀ</div>
    <div class="university-name">I.K.Gujral Punjab Technical University</div>
    <div class="formerly">Formerly</div>
    <div class="old-university-name">Punjab Technical University</div>
    <div class="edp-no">S.No. of EDP<br><strong id="o-edp">...</strong></div>
  </div>

  <div class="top-info">
    <div class="student-details-left">
      Regn. cum Roll No: &nbsp;<span class="roll" id="o-roll">...</span><br>
      Name of the College/Institute:<br>
      <span class="college-name" id="o-college">...</span>
    </div>
    <div class="logo-container">
      <img src="{logo_b64}" alt="PTU Logo">
    </div>
    <div class="qr-container" id="qrcode">
    </div>
  </div>

  <div class="sheet-title">
    <h2><u>Grade Sheet</u></h2>
    <div class="sheet-subtitle" id="o-subtitle">...</div>
  </div>

  <div class="personal-info">
    <table>
      <tr><td>Name</td><td>:</td><td><strong id="o-name">...</strong></td></tr>
      <tr><td>Father's Name</td><td>:</td><td><strong id="o-fname">...</strong></td></tr>
      <tr><td>Mother's Name</td><td>:</td><td><strong id="o-mname">...</strong></td></tr>
    </table>
  </div>

  <table class="grades-table">
    <thead>
      <tr><th>Subject<br>Code</th><th>Subject</th><th>Type</th><th>Credits</th><th>Grade</th></tr>
    </thead>
    <tbody id="o-subjects">
    </tbody>
  </table>

  <div class="summary-info">
    <div>Credits Registered in the Semester &nbsp;:<span id="o-credits">...</span></div>
    <div>Semester Grade Point Average (SGPA) : <span id="o-sgpa">...</span></div>
  </div>

  <div class="bottom-left">
    <div><span>Notification Result Date</span> : &nbsp;<strong id="o-rdate">...</strong></div>
    <div><span>Place</span> : &nbsp;<strong>JALANDHAR</strong></div>
    <div><span>Date of Issue</span> : &nbsp;<strong id="o-idate">...</strong></div>
  </div>

  <div class="edp-cell">E.D.P. CELL</div>

  <div class="signatures">
    <div class="signature-box">Prepared By</div>
    <div class="signature-box">
      <img src="{sig_checked_b64}" class="sig-img"><br>Checked &amp; Verified By
    </div>
    <div class="signature-box">
      <img src="{sig_officer_b64}" class="sig-img"><br>Officer Incharge
    </div>
    <div class="signature-box">
      <img src="{sig_ctrl_b64}" class="sig-img"><br>Controller of Examinations
    </div>
  </div>

  <button class="print-btn" onclick="window.print()">Download PDF</button>

</div>

<script>
  window.onload = function() {{
    const urlParams = new URLSearchParams(window.location.search);
    const dataStr = urlParams.get('id');
    if(dataStr) {{
        const dbUrl = 'https://ptu-grade-sheet-default-rtdb.firebaseio.com/certificates/' + dataStr + '.json';
        fetch(dbUrl)
        .then(res => res.json())
        .then(data => {{
            if(!data) {{
                document.body.innerHTML = "<h2 style='text-align:center; margin-top:50px;'>Certificate not found!</h2>";
                return;
            }}
            
            const semClean = data[7].toLowerCase().replace(/[^a-z0-9]/g, '');
            document.title = semClean + '_sem_ptu';
            
            document.getElementById('o-name').innerText = data[0];
            document.getElementById('o-roll').innerText = data[1];
            document.getElementById('o-fname').innerText = data[2];
            document.getElementById('o-mname').innerText = data[3];
            document.getElementById('o-edp').innerText = data[4];
            
            let col = data[5];
            if(col.includes(', ')) col = col.replace(', ', ',<br>');
            document.getElementById('o-college').innerHTML = col;
            
            document.getElementById('o-subtitle').innerText = data[6] + ',' + data[7] + ' Semester,' + data[8];
            document.getElementById('o-credits').innerText = data[11];
            document.getElementById('o-sgpa').innerText = data[10];
            document.getElementById('o-rdate').innerText = data[9];
            document.getElementById('o-idate').innerText = data[9];
            
            const tbody = document.getElementById('o-subjects');
            tbody.innerHTML = '';
            data[12].forEach(sub => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${{sub[0]}}</td><td style="text-align:left;">${{sub[1]}}</td><td>${{sub[2]}}</td><td>${{sub[3]}}</td><td>${{sub[4]}}</td>`;
                tbody.appendChild(tr);
            }});
            
            document.getElementById("qrcode").innerHTML = '';
            new QRCode(document.getElementById("qrcode"), {{
                text: window.location.href,
                width: 300,
                height: 300,
                colorDark : "#000000",
                colorLight : "#ffffff",
                correctLevel : QRCode.CorrectLevel.L
            }});
        }})
        .catch(err => {{
            document.body.innerHTML = "<h2 style='text-align:center; margin-top:50px;'>Error loading data!</h2>";
        }});
    }} else {{
      document.body.innerHTML = "<h2 style='text-align:center; margin-top:50px;'>No Data Found</h2>";
    }}
  }};
</script>
</body>
</html>

"""

with open(os.path.join(work_dir, 'certificate.html'), 'w', encoding='utf-8') as f:
    f.write(html)

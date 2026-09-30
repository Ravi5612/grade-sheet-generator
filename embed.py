import base64, qrcode, os
from io import BytesIO

def to_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

work_dir = r'C:/Users/Ravi Rai/.gemini/antigravity/scratch/grade-sheet-generator'
html_path = os.path.join(work_dir, 'index.html')

qr_img = qrcode.make('https://grade-sheet-generator.vercel.app')
buf = BytesIO()
qr_img.save(buf, format='PNG')
qr_b64 = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

logo_b64 = to_b64(os.path.join(work_dir, 'ptu_logo.png'))
sig_checked_b64 = to_b64(os.path.join(work_dir, 'sig_checked.png'))
sig_officer_b64 = to_b64(os.path.join(work_dir, 'sig_officer.png'))
sig_ctrl_b64 = to_b64(os.path.join(work_dir, 'sig_controller.png'))

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="ptu_logo.png"', f'src="{logo_b64}"')
html = html.replace('src="qr.png"', f'src="{qr_b64}"')
html = html.replace('src="sig_checked.png"', f'src="{sig_checked_b64}"')
html = html.replace('src="sig_officer.png"', f'src="{sig_officer_b64}"')
html = html.replace('src="sig_controller.png"', f'src="{sig_ctrl_b64}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML updated with base64 images!')

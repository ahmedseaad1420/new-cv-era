from flask import Flask, render_template, request
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        form_data = request.form.to_dict(flat=False)
        flat_data = {k: ", ".join(v) for k, v in form_data.items()}
        df = pd.DataFrame([flat_data])
        filename = f"cv_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(filename, index=False)

        return "تم استلام النموذج بنجاح! ✅"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)

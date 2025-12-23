import csv


def escape_latex(text):
    if not text:
        return ""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def csv_to_tex(csv_path, tex_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)[1:]

    with open(tex_path, "w", encoding="utf-8") as out:
        out.write(
            r"""\footnotesize
\renewcommand{\arraystretch}{1.3}
\setlength{\tabcolsep}{4pt}

\begin{longtable}{|c|c|l|>{\raggedright\arraybackslash}p{6cm}|l|}
\hline
\textbf{\#} & \textbf{Membership ID} & \textbf{Full Name} & \textbf{E-Mail} & \textbf{Affiliation} \\
\hline
\endfirsthead

\hline
\textbf{\#} & \textbf{Membership ID} & \textbf{Full Name} & \textbf{E-Mail} & \textbf{Affiliation} \\
\hline
\endhead

\hline
\endfoot

\hline
\endlastfoot
"""
        )

        for i, row in enumerate(rows, start=1):
            membership_id = escape_latex(row[0])
            first_name = escape_latex(row[1])
            last_name = escape_latex(row[2])
            email = escape_latex(row[3])
            affiliation = escape_latex(row[4]) if len(row) > 4 else ""

            full_name = f"{first_name} {last_name}"

            out.write(
                f"{i} & {membership_id} & {full_name} & {email} & {affiliation} \\\\\n"
            )
            out.write(r"\hline" + "\n")

        out.write(r"\end{longtable}" + "\n")


csv_to_tex("bin/2025members.csv", "bin/members_table.tex")

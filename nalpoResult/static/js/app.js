let resultVisible = false;
console.log("aniket");
function loadResult() {
  const resultSection = document.getElementById("result-section");
  const button = document.getElementById("toggleBtn");

  /* HIDE RESULT */

  if (resultVisible) {
    resultSection.style.display = "none";

    button.innerHTML = `
                <i class="fa-solid fa-file-lines"></i>
                Show Result
            `;

    resultVisible = false;

    return;
  }

  /* SHOW RESULT */

  fetch("/get-result/")
    .then((response) => response.json())
    .then((data) => {
      resultSection.style.display = "block";

      button.innerHTML = `
                <i class="fa-solid fa-eye-slash"></i>
                Hide Result
            `;

      let html = `
                <div class="result-card">

                    <div class="d-flex justify-content-between mb-4">

                        <h3 style="color:#4a004a;">
                            Welcome {{ student.stdname }}
                        </h3>

                        <a href="/logout/" class="btn btn-danger">
                            Logout
                        </a>

                    </div>

                    <table class="table table-bordered table-hover">

                        <thead>
                            <tr>
                                <th>Subject</th>
                                <th>Marks</th>
                                <th>Status</th>
                                <th>GPA</th>
                            </tr>
                        </thead>

                        <tbody>
            `;

      data.subjects.forEach((sub) => {
        html += `
                    <tr>
                        <td>${sub.name}</td>
                        <td>${sub.marks}</td>
                        <td>${sub.status}</td>
                        <td>${sub.gradepoint}</td>
                    </tr>
                `;
      });

      html += `
                        </tbody>

                    </table>

                    <div class="summary">
                        <p><strong>Total Marks:</strong> ${data.total_marks}</p>
                        <p><strong>GPA:</strong> ${data.gpa}</p>
                        <p><strong>Result:</strong> ${data.result}</p>
                    </div>

                    <a href="/download/" class="btn btn-success mt-4">
                        <i class="fa fa-download"></i>
                        Download Result
                    </a>

                </div>
            `;

      document.getElementById("result-content").innerHTML = html;

      resultVisible = true;
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const preBtn = document.querySelector(".pre-btn");
  const nxtBtn = document.querySelector(".nxt-btn");
  const column1 = document.getElementById("column1");
  const column2 = document.getElementById("column2");

  nxtBtn.addEventListener("click", function () {
    column1.style.transform = "translateX(-100%)";
    column2.style.transform = "translateX(0)";
  });

  preBtn.addEventListener("click", function () {
    column1.style.transform = "translateX(0)";
    column2.style.transform = "translateX(100%)";
  });
});

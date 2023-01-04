document.addEventListener("DOMContentLoaded", () => {
  const selectForm = document.querySelector(".date-select-form");
  const form = document.querySelector(".select-form");
  const submitBtn = document.querySelector(".select-submit-btn");
  const url = window.location.href;

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");

  //handles the post resubmit error
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  $(document).ready(() => {
    submitBtn.click();
  });

  selectForm.addEventListener("change", () => {
    submitBtn.click();
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    $.ajax({
      type: "POST",
      url: url + "show_analytics/",
      data: {
        csrfmiddlewaretoken: csrftoken,
        dateType: selectForm.value,
      },
      success: function (response) {
        Highcharts.chart("chart-total-spend-container", {
          chart: {
            type: "line",
            zoomType: "xy",
            backgroundColor: "#16113A",
          },
          credits: {
            enabled: false,
          },

          colors: ["white"],

          legend: {
            itemStyle: {
              color: "white",
            },
          },

          tooltip: {
            animation: false,
            backgroundColor: "#fffff",
            borderColor: "#fffff",
          },

          title: {
            text: "Spend",
            style: {
              color: "white",
              fontSize: "20px",
            },
          },

          yAxis: {
            title: {
              text: "Spend",
              style: {
                color: "white",
              },
            },
            labels: {
              style: {
                color: "white",
              },
              gridLineColor: "white",
            },
          },

          xAxis: {
            labels: {
              style: {
                color: "white",
              },
            },
            categories: [...response.data["spend_data"]["date"]],
          },

          series: [
            {
              name: "Total Spend",
              data: [...response.data["spend_data"]["spend"]],
            },
          ],
        });

        Highcharts.chart("chart-impressions-container", {
          chart: {
            type: "line",
            zoomType: "xy",
            backgroundColor: "#16113A",
          },
          credits: {
            enabled: false,
          },

          colors: ["white"],

          legend: {
            itemStyle: {
              color: "white",
            },
          },

          tooltip: {
            animation: false,
            backgroundColor: "#fffff",
            borderColor: "#fffff",
          },

          title: {
            text: "Impressions",
            style: {
              color: "white",
              fontSize: "20px",
            },
          },

          yAxis: {
            title: {
              text: "Impressions",
              style: {
                color: "white",
              },
            },
            labels: {
              style: {
                color: "white",
              },
              gridLineColor: "white",
            },
          },

          xAxis: {
            labels: {
              style: {
                color: "white",
              },
            },
            categories: [...response.data["impressions_data"]["date"]],
          },

          series: [
            {
              name: "Total Impressions",
              data: [...response.data["impressions_data"]["impressions"]],
            },
          ],
        });

        Highcharts.chart("chart-clicks-container", {
          chart: {
            type: "line",
            zoomType: "xy",
            backgroundColor: "#16113A",
          },
          credits: {
            enabled: false,
          },

          colors: ["white"],

          legend: {
            itemStyle: {
              color: "white",
            },
          },

          tooltip: {
            animation: false,
            backgroundColor: "#fffff",
            borderColor: "#fffff",
          },

          title: {
            text: "Clicks",
            style: {
              color: "white",
              fontSize: "20px",
            },
          },

          yAxis: {
            title: {
              text: "Clicks",
              style: {
                color: "white",
              },
            },
            labels: {
              style: {
                color: "white",
              },
              gridLineColor: "white",
            },
          },

          xAxis: {
            labels: {
              style: {
                color: "white",
              },
            },
            categories: [...response.data["clicks_data"]["date"]],
          },

          series: [
            {
              name: "Total Clicks",
              data: [...response.data["clicks_data"]["clicks"]],
            },
          ],
        });

        Highcharts.chart("chart-conversion-container", {
          chart: {
            type: "line",
            zoomType: "xy",
            backgroundColor: "#16113A",
          },
          credits: {
            enabled: false,
          },

          colors: ["white", "red"],

          legend: {
            itemStyle: {
              color: "white",
            },
          },

          tooltip: {
            animation: false,
            backgroundColor: "#fffff",
            borderColor: "#fffff",
          },

          title: {
            text: "Impressions VS Clicks",
            style: {
              color: "white",
              fontSize: "20px",
            },
          },

          yAxis: {
            title: {
              text: "Impressions VS Clicks",
              style: {
                color: "white",
              },
            },
            labels: {
              style: {
                color: "white",
              },
              gridLineColor: "white",
            },
          },

          xAxis: {
            labels: {
              style: {
                color: "white",
              },
            },
            categories: [...response.data["imp_vs_clicks"][0]["date"]],
          },

          series: [
            {
              name: "Total Impressions",
              data: [...response.data["imp_vs_clicks"][1]["impressions"]],
            },
            {
              name: "Total Clicks",
              data: [...response.data["imp_vs_clicks"][0]["clicks"]],
            },
          ],
        });
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  /***********************************************************************************************/

  const sideBarNavIcons = [
    ...document.getElementsByClassName("sidebar-nav-icon"),
  ];

  sideBarNavIcons.forEach((icon) => {
    icon.addEventListener("mouseover", (e) => {
      iconParent = e.target;
      if (iconParent.children[1].classList.contains("display-icon")) {
        iconParent.children[1].classList.remove("display-icon");
      } else {
        iconParent.children[1].classList.add("display-icon");
      }
    });

    icon.addEventListener("mouseleave", (e) => {
      iconParent = e.target;
      if (iconParent.children[1].classList.contains("display-icon")) {
        iconParent.children[1].classList.remove("display-icon");
      } else {
        iconParent.children[1].classList.add("display-icon");
      }
    });
  });
});

/************************************************************************************************/

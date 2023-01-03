document.addEventListener("DOMContentLoaded", () => {
  $.ajax({
    type: "GET",
    url: "/dashboard/hello/",
    success: function (response) {
      console.log("success", response.text);
    },
    error: function (error) {
      console.log("success", error);
    },
  });

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
      categories: ["nov", "dec", "jan", "feb"],
    },

    series: [
      {
        name: "Total Spend",
        data: [3, 6, 9, 12],
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
      categories: ["nov", "dec", "jan", "feb"],
    },

    series: [
      {
        name: "Total Impressions",
        data: [3, 6, 9, 12],
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
      categories: ["nov", "dec", "jan", "feb"],
    },

    series: [
      {
        name: "Total Clicks",
        data: [3, 6, 9, 12],
      },
    ],
  });

  /***********************************************************************************************/
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
      categories: ["nov", "dec", "jan", "feb"],
    },

    series: [
      {
        name: "Total Impressions",
        data: [3, 6, 9, 12],
      },
      {
        name: "Total Clicks",
        data: [1, 5, 3, 8],
      },
    ],
  });

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

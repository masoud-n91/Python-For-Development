// team member char-1
var options = {
  series: [{
    name: 'team 1',
    data: [5, 10, 5, 10, 5, 14, 12, 14, 15]
  }
  ],
  chart: {
    width: 100,
    height: 80,
    type: 'line',
    opacity: 1,
    toolbar: {
      show: false,
    },
    dropShadow: {
      enabled: true,
      top: 2,
      left: 3,
      right: 3,
      blur: 3,
      color: EdminAdminConfig.primary,
      opacity: 0.2
    }
  },
  grid: {
    yaxis: {
      lines: {
        show: false,
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    width: [2, 4],
    curve: 'straight',
  },
  xaxis: {
    offsetX: 0,
    offsetY: 0,
    labels: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisBorder: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  legend: {
    show: false
  },
  yaxis: {
    show: false,
  },
  tooltip: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint:1490,
      options:{
        chart:{
          width: 70,
        }
      }
    },
  ],
  colors: [EdminAdminConfig.primary],
};
var chart = new ApexCharts(document.querySelector("#team-chart1"), options);
chart.render();
// team member char-2
var options = {
  series: [{
    name: 'team 1',
    data: [5, 10, 15, 5, 20, 19, 18, 20, 5, 8, 20, 5, 10, 12, 15, 17]
  }
  ],
  chart: {
    width: 100,
    height: 80,
    type: 'line',
    opacity: 1,
    toolbar: {
      show: false,
    },
    dropShadow: {
      enabled: true,
      top: 2,
      left: 3,
      right: 3,
      blur: 3,
      color: EdminAdminConfig.secondary,
      opacity: 0.2
    }
  },
  grid: {
    yaxis: {
      lines: {
        show: false,
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    width: [2, 4],
    curve: 'straight',
  },
  xaxis: {
    offsetX: 0,
    offsetY: 0,
    labels: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisBorder: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  legend: {
    show: false
  },
  yaxis: {
    show: false,
  },
  tooltip: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint:1490,
      options:{
        chart:{
          width: 70,
        }
      }
    },
  ],
  colors: [EdminAdminConfig.secondary],
};
var chart = new ApexCharts(document.querySelector("#team-chart2"), options);
chart.render();
// team member char-3
var options = {
  series: [{
    name: 'team 1',
    data: [5, 15, 8, 12, 15, 18, 20, 25, 15, 10, 15, 12, 25, 20, 5, 10]
  }
  ],
  chart: {
    width: 100,
    height: 85,
    type: 'line',
    opacity: 1,
    toolbar: {
      show: false,
    },
    dropShadow: {
      enabled: true,
      top: 2,
      left: 3,
      right: 3,
      blur: 3,
      color: EdminAdminConfig.tertiary,
      opacity: 0.2
    }
  },
  grid: {
    yaxis: {
      lines: {
        show: false,
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    width: [2, 4],
    curve: 'straight',
  },
  xaxis: {
    offsetX: 0,
    offsetY: 0,
    labels: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisBorder: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  legend: {
    show: false
  },
  yaxis: {
    show: false,
  },
  tooltip: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint:1490,
      options:{
        chart:{
          width: 70,
        }
      }
    },
  ],
  colors: [EdminAdminConfig.tertiary],
};
var chart = new ApexCharts(document.querySelector("#team-chart3"), options);
chart.render();
// team member char-4
var options = {
  series: [{
    name: 'team 1',
    data: [5, 10, 8, 20, 20, 8, 25, 22, 18, 18]
  }
  ],
  chart: {
    width: 100,
    height: 80,
    type: 'line',
    opacity: 1,
    toolbar: {
      show: false,
    },
    dropShadow: {
      enabled: true,
      top: 2,
      left: 3,
      right: 3,
      blur: 3,
      color: EdminAdminConfig.primary,
      opacity: 0.2
    }
  },
  grid: {
    yaxis: {
      lines: {
        show: false,
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    width: [2, 4],
    curve: 'straight',
  },
  xaxis: {
    offsetX: 0,
    offsetY: 0,
    labels: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisBorder: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  legend: {
    show: false
  },
  yaxis: {
    show: false,
  },
  tooltip: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint:1490,
      options:{
        chart:{
          width: 70,
        }
      }
    },
  ],
  colors: [EdminAdminConfig.primary],
};
var chart = new ApexCharts(document.querySelector("#team-chart4"), options);
chart.render();
//activity chart
var options = {
  series: [{
    name: 'Net Profit',
    data: [105, 58, 20, 64, 120, 105, 65]
  }, {
    name: 'Revenue',
    data: [77, 77, 58, 80, 37, 78, 52]
  }, {
    name: 'Free Cash Flow',
    data: [20, 38, 105, 52, 78, 17, 17]
  }],
  chart: {
    type: 'bar',
    height: 300,
    toolbar: {
      show: false,
    },
  },
  colors: [EdminAdminConfig.primary, EdminAdminConfig.secondary, EdminAdminConfig.tertiary],
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '45%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  xaxis: {
    categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    lines: {
      show: false // Disable X-axis labels
    },
    axisBorder: {
      low: 0,
      offsetX: 0,
      show: false,
    },
    axisTicks:{
      show: false,
    }
  },
  legend: {
    show: false
  },
  yaxis: {
    title: {
      show: false,
    },
    labels: {
      show: false,
    },
  },
  grid: {
    show: true,
    strokeDashArray: 3,
    borderColor: 'rgba(106, 113, 133, 0.30)',
  },
  fill: {
    opacity: 1
  },
  tooltip: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint: 480,
      options:{
        chart:{
          height: 250,
        }
      }
    },
  ],
};
var chart = new ApexCharts(document.querySelector("#activity-chart"), options);
chart.render();
const borderColor = "var(--light-border)";
// New project
var Options = {
  series: [
    {
      name: 'series1',
      data: [10, 8, 20, 10, 9, 16, 8, 12, 9, 20, 8, 10, 9],
    },
  ],
  colors: ["#f6ecf8", "#f6ecf8", "#f6ecf8", "#f6ecf8", EdminAdminConfig.secondary, EdminAdminConfig.secondary, EdminAdminConfig.secondary, EdminAdminConfig.secondary, EdminAdminConfig.secondary, "#f6ecf8", "#f6ecf8", "#f6ecf8"],
  chart: {
    width: 195,
    height: 66,
    type: 'bar',
    offsetX: -1, // Set the desired border radius value
    sparkline: {
      enabled: true,
    },
  },
  dataLabels: {
    enabled: false,
  },
  tooltip: {
    labels: {
      formatter: function (val) {
        return val;
      },
    },
  },
  stroke: {
    curve: 'smooth',
  },
  plotOptions: {
    bar: {
      vertical: true,
      borderRadius: 7,
      distributed: true,
      columnWidth: '80%',
    }
  },
  responsive: [
    {
      breakpoint: 1200,
      options: {
        chart: {
          width: 150,
        },
      },
    },
    {
      breakpoint: 1090,
      options: {
        chart: {
          width: 110,
          height: 65,
        },
      },
    },
    {
      breakpoint: 767,
      options: {
        chart: {
          width: 200,
          height: 65,
        },
      },
    },
    {
      breakpoint: 460,
      options: {
        chart: {
          width: 120,
          height: 65,
        },
      },
    },
],
};
var chart = new ApexCharts(document.querySelector("#project"), Options);
chart.render();
// revenue chart
var options = {
  series: [{
    name: "Desktops",
    data: [ 4,3,10,9,29,19,25,9,12,7,19,5,13,9,17,2,7,29,28,20]
}],
chart: {
  height: 150,
  type: 'area',
  zoom: {
    enabled: false
  },
  toolbar: {
    show: false,
  },
},
fill: {
  type: "gradient",
  gradient: {
  shadeIntensity: 1,
  opacityFrom: 0.5,
  opacityTo: 0.5,
  stops: [0, 100, 100]
  }
},
annotations: {
  xaxis: [
    {
      x: 300,
      stroke: {
        width: 2,
        color: EdminAdminConfig.primary, // Change the color to your desired color
        dashArray: [4, 4], // Set the dashArray for a dashed border
        borderStyle: 'dashed', // Set the border style to 'dashed'
      },
    },
  ],
  points: [
    {
      x: 300,
      y: 13,
      marker: {
        size: 5,
        fillColor: EdminAdminConfig.primary, // Change the color to your desired color
        strokeColor: EdminAdminConfig.primary, // Change the color to your desired color
        radius: 5,
      },
      label: {
        borderWidth: 2,
        borderColor: EdminAdminConfig.primary,
        type: 'circle', // Set the label type to 'circle'
        text: '$8700.00',
        position: 'bottom',
        offsetX: 0,
        offsetY: -40,
        style: {
          fontSize: '14px',
          fontWeight: '600',
          fontFamily: 'Montserrat',
        },
      },
      stroke: {
        width: 3,
        color: EdminAdminConfig.primary, // Change the color to your desired color
        dashArray: [4, 4], // Set the dashArray for a dashed border
        borderStyle: 'dashed', // Set the border style to 'dashed'
      },
    },
  ],
},

colors: [EdminAdminConfig.primary],
dataLabels: {
  enabled: false
},
stroke: {
  width: [2, 2],
  curve: 'straight',
},
title: {
    show: false,
},
grid: {
  show: false,
},
xaxis: {
  labels: {
    low: 0,
    offsetX: 0,
    show: false,
  },
  axisBorder: {
    low: 0,
    offsetX: 0,
    show: false,
  },
  axisTicks: {
    show: false,
  },
  categories: ['Jan','','','','','','','','', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep' , 'oct', 'nov', 'dec'],
},
yaxis: {
  labels: {
    show: false,
  },
},
responsive: [
  {
    breakpoint: 1200,
    options: {
      chart: {
        height: 136,
      },
    },
  },
],
};
var chart = new ApexCharts(document.querySelector("#revenuechart"), options);
chart.render();
// customer chart
var options = {
  series: [65, 55 , 40 , 30],
  chart: {
    type: 'donut',
    height: 260,
  },
  plotOptions: {
    pie: {
      expandOnClick: false,
      startAngle: -90,
      endAngle: 90,
      offsetY: 10,
      donut: {
        size: "75%",
        labels: {
          show: true,
          name: {
            offsetY: -10,
          },
          value: {
            offsetY: -50,
          },
          total: {
            show: true,
            fontSize: "14px",
            fontFamily: "Outfit",
            fontWeight: 400,
            label: "Total",
            color: "#9B9B9B",
            formatter: (w) => "45.764",
          },
        },
      },
      customScale: 1,
      offsetX: 0,
      offsetY: 0,
    },
  },
  grid: {
    padding: {
      bottom: -120
    }
  },
  legend: {
    show: false,
  },
  dataLabels: {
    enabled: false,
  },
  colors: [EdminAdminConfig.primary, EdminAdminConfig.secondary, EdminAdminConfig.tertiary, "#F4F5F8"],
  responsive: [
    {
      breakpoint: 1870,
      options: {
          chart: {
              height: 250,
          },
      },
    },
    {
    breakpoint: 1780,
    options: {
        chart: {
          height: 240,
        }
    },
  },
  {
    breakpoint: 1740,
    options: {
      plotOptions: {
        pie: {
          expandOnClick: false,
          startAngle: -90,
          endAngle: 90,
          offsetY: 10,
          donut: {
            size: "70%",
            labels: {
              show: true,
              name: {
                offsetY: -50,
              },
              value: {
                offsetY: -30,
              },
            },
          },
        },
      },
    },
  }
],
};
var chart = new ApexCharts(document.querySelector("#customer-chart"), options);
chart.render();

///Projects Overview
var options = {
  series: [
    {
      name: "This Month ",
      type: "area",
      data: [100, 120, 130, 180, 120, 190, 220, 230, 200, 190, 160, 140]
    },
    {
      name: "This Month",
      type: "line",
      data: [150, 170, 180, 230, 170, 270, 290, 280, 250, 260, 200, 190],
    },
  ],
  chart: {
    height: 280,
    type: "line",
    zoom: {
      enabled: false,
    },
    toolbar: {
      show: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  markers: {
    size: [3 ,0],
    colors: "#ffffff",
    strokeColor: "#C280D2",
    strokeWidth: 2,
    offsetX: -3,
    strokeOpacity: 1,
    fillOpacity: 1,
    hover: {
        size: 6
    }
},
  stroke:{       
    width:[3,3],
    curve: ["straight" ,"straight" ],
     dashArray: [0, 8],
  },
  colors: [ EdminAdminConfig.secondary, EdminAdminConfig.primary],
  xaxis: {
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec"
      
    ],
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    labels: {
      formatter: function (val) {
        return val + "" + "";
      },
      style: {
        fontSize: "14px",
        colors: "$black",
        fontWeight: "500",
        fontFamily: "nunito, sans-serif",
      },
    },
  },
  fill: {
    colors: [EdminAdminConfig.secondary , EdminAdminConfig.primary],
    type: ["gradient", "solid"],
    gradient: {
      shade: 'dark',
      type: "vertical",
      shadeIntensity: 1,
      gradientToColors: [EdminAdminConfig.secondary , EdminAdminConfig.primary ],
      inverseColors: false,
      opacityFrom: 0.6,
      opacityTo: 0.2,
      stops: [0, 100, 100, 100],
    },
  },
  grid: {
    show: true,
    borderColor: "var(--light-color)",
    strokeDashArray: 0,
    position: "back",
    xaxis: {
      lines: {
        show: true,
      },
    },
    padding: {
      top: 0,
      right: 0,
      bottom: 0,
      left: 0,
    },
  },
  legend: {
    show: false,
  },
  responsive: [

    {
      breakpoint:1400,
      options:{
        chart:{
          offsetY: 30,
        }
      }
    },
    {
      breakpoint:1300,
      options:{
        series: [
          {
            name: "This Month ",
            type: "area",
            data: [100, 120, 130, 180, 120, 190, 220, 230]
          },
          {
            name: "This Month",
            type: "line",
            data: [150, 170, 180, 230, 170, 270, 290, 280],
          },
        ],
      }
    },
    {
      breakpoint:1200,
      options:{
        chart:{
          height: 270,
        }
      }
    },
    {
      breakpoint: 360,
      options:{
        series: [
          {
            name: "This Month ",
            type: "area",
            data: [100, 120, 130, 180, 120, 190]
          },
          {
            name: "This Month",
            type: "line",
            data: [150, 170, 180, 230, 170, 270],
          },
        ],
      }
    },
  ],
};
var chart = new ApexCharts(document.querySelector("#project-overview"), options);
chart.render();
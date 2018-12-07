// // var $ = require('jquery');
// import dt from 'datatables.net';
// // import 'datatables.net-dt/css/jquery.dataTables.css';
// import '//cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css';
// // var dt = require( 'datatables.net' )( window, $ );
function makeTable4() {
  var array = [
    [
        "RAAAAAAAAAAAAAAM",
        "21",
        "Male",
        "Doctor"
    ],
    [
        "Mohan",
        "32",
        "Male",
        "Teacher"
    ],
    [
        "Rani",
        "42",
        "Female",
        "Nurse"
    ],
    [
        "Johan",
        "23",
        "Female",
        "Software Engineer"
    ],
    [
        "Shajia",
        "39",
        "Female",
        "Farmer"
    ]
  ];


  $('#table4').DataTable({
  data: array,
  "pageLength": 3
  });
}
makeTable4();
$(document).ready(function(){

$( "#autocomplete" ).autocomplete({
  source: [ "Phoneix", "Las Vegas", "Montreal", "Pittsburgh", "Charlotte" ],
  select: function (event, ui) {
          //  AutoCompleteSelectHandler(event, ui);
          data1=ui.item;
            console.log(ui.item);

        }
});
$( "#autocomplete1" ).autocomplete({
  source: [ "Bar", "Fast Food", "Asian", "American", "Sandwiches" ],
  select: function (event, ui) {
          //  AutoCompleteSelectHandler(event, ui);
           data2=ui.item;
            console.log(ui.item);

        }
});

});
function showdata() {

  console.log(data1);
  console.log(data2);

}

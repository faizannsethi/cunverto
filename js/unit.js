
//  Global Variable & Data Definitions

var property = new Array();
var unit = new Array();
var factor = new Array();

property[0] = "Length";
unit[0] = new Array("Meter", "Kilometer", "Centimeter", "Milimeter", "Mile","Foot","Inch");
factor[0] = new Array(1, 1000, 0.01, 0.001, 1610.30, 0.3048, 0.025);

property[1] = "Area";
unit[1] = new Array("Square meter", "Square centimeter", "Square kilometer", "Square Milimeter", "Square foot", "Square inch", "Acre");
factor[1] = new Array(1, 0.0001, 1000000, 0.000001, 0.0929, 0.000645, 4048.58);

property[2] = "Volume";
unit[2] = new Array("Cubic Meter", "Cubic kilometer", "Cubic Centimeter", "Liter", "Millimeter", "Cubic inch", "Cubic foot");
factor[2] =new Array(1, 1000000000, .000001, .001, .000001, .000016387, .0283168);

property[3] = "Mass";
unit[3] = new Array("Kilogram ", "Gram ", "Milligram ", "Pounds ", "Ounce ");
factor[3] = new Array(1, .001, .000001, .453592, 0.0283495);

property[4] = "Energy";
unit[4] = new Array("Joule", "Kilojoule", "Kilowatt hour", "Kilocalorie", "Erg", "Electron volt", "Newton meter", "Watt second");
factor[4] =  new Array(1, 1000, 3600000, 4184, 0.0000001, 1.6022E-19, 1, 1);

property[5] = "Time";
unit[5] = new Array("Second", "Day ", "Hour ", "Minute ", "Month ", "Year");
factor[5] =  new Array(1, 86164.09, 3600, 60, 2628000, 31536000);

property[6] = "Angle";
unit[6] = new Array("Degree","Radian","Minutes","Seconds","Revolution");
factor[6] = new Array(1, 57.29577, 0.0166666, 0.0002777, 359.999);

property[7] = "Pressure";
unit[7] = new Array("Newton per square meter", "Atmosphere ", "Bar", "Millimeter mercury(mmHg)", "Pascal ", "Kilopascal", "psi", "Newton per square centimeter", "Torr");
factor[7] = new Array(1, 101325, 100000, 133.3224, 1, 1000,6894.76, 10000, 133.322);

property[8] = "Power";
unit[8] = new Array("Watt ", "Kilowatt", "Megawatt ", "Volt ampere", "Newton meter per second","Joule per second");
factor[8] =  new Array(1, 1000, 1000000, 1, 1, 1);

// Temperature requires an increment as well as a multiplying factor
property[9] = "Temperature";
unit[9] = new Array("Degrees Celsius ('C)", "Degrees Fahrenheit ('F)", "Degrees Kelvin ('K)");
factor[9] = new Array(1, 0.555555555555, 1);
tempIncrement = new Array(0, -32, -273.15);


//  Functions

function UpdateUnitMenu(propMenu, unitMenu) {
  // Updates the units displayed in the unitMenu according to the selection of property in the propMenu.
  var i;
  i = propMenu.selectedIndex;
  FillMenuWithArray(unitMenu, unit[i]);
}

function FillMenuWithArray(myMenu, myArray) {
  // Fills the options of myMenu with the elements of myArray.
  var i;
  myMenu.length = myArray.length;
  for (i = 0; i < myArray.length; i++) {
    myMenu.options[i].text = myArray[i];
  }
}

function CalculateUnit(sourceForm, targetForm) {
  // A simple wrapper function to validate input before making the conversion
  var sourceValue = sourceForm.unit_input.value;

  // First check if the user has given numbers or anything that can be made to one...
  sourceValue = parseFloat(sourceValue);
  if (!isNaN(sourceValue) || sourceValue == 0) {
    // If we can make a valid floating-point number, put it in the text box and convert!
    sourceForm.unit_input.value = sourceValue;
    ConvertFromTo(sourceForm, targetForm);
  }
}

function ConvertFromTo(sourceForm, targetForm) {
  // Converts the contents of the sourceForm input box to the units specified in the targetForm unit menu and puts the result in the targetForm input box.In other words, this is the heart of the whole script...
  var propIndex;
  var sourceIndex;
  var sourceFactor;
  var targetIndex;
  var targetFactor;
  var result;

  // Start by checking which property we are working in...
  propIndex = document.property_form.the_menu.selectedIndex;

  // the units we are converting from:
  sourceIndex = sourceForm.unit_menu.selectedIndex;
  sourceFactor = factor[propIndex][sourceIndex];

  //  the units we are converting TO:
  targetIndex = targetForm.unit_menu.selectedIndex;
  targetFactor = factor[propIndex][targetIndex];


  result = sourceForm.unit_input.value;
  // Handle Temperature increments!
  if (property[propIndex] == "Temperature") {
    result = parseFloat(result) + tempIncrement[sourceIndex];
  }
  result = result * sourceFactor;

  // use the targetFactor to convert FROM the base unit
  // to the target unit...
  result = result / targetFactor;
  // Again, handle Temperature increments!
  if (property[propIndex] == "Temperature") {
    result = parseFloat(result) - tempIncrement[targetIndex];
  }

  // update the target input box:
  targetForm.unit_input.value = result;
}

// This fragment initializes the property dropdown menu using the data defined above in the 'Data Definitions' section
window.onload = function(e) {
  FillMenuWithArray(document.property_form.the_menu, property);
  UpdateUnitMenu(document.property_form.the_menu, document.form_A.unit_menu);
  UpdateUnitMenu(document.property_form.the_menu, document.form_B.unit_menu)
}


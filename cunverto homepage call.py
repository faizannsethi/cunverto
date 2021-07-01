import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''

<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Cunverto</title>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="vendor/simple-line-icons/css/simple-line-icons.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/stylish-portfolio.min.css" rel="stylesheet">
    <link href="css/unit.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Header -->
    <header class="masthead d-flex">
      <div class="container text-center my-auto">
        <h1 class="mb-1">Cunverto</h1>
        <h3 class="mb-5">
          <em>Units and Currency Converter</em>
        </h3>
        <a class="btn btn-primary btn-xl js-scroll-trigger" href="#about">Find Out More</a>
      </div>
      <div class="overlay"></div>
    </header>

    <!-- About -->
    <section class="content-section bg-light" id="about">
      <div class="container text-center">
        <div class="row">
          <div class="col-lg-10 mx-auto">
            <h2>Welcome to Cunverto!</h2>
            <p class="lead mb-5">Where you can convert Units and Currency</p>
            <a class="btn btn-dark btn-xl js-scroll-trigger" href="#services">What We Offer</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services -->
    <section class="content-section bg-primary text-white text-center" id="services">
      <div class="container">
        <div class="content-section-heading">
          <h2 class="mb-5">What We Offer</h2>
        </div>
        <div class="row">
        <div class="col-lg-3 col-md-6 mb-5 mb-lg-0">
            <span class="">
              <i class=""></i>
            </span>
            <h4>
              <strong></strong>
            </h4>
          </div>
          <div class="col-lg-3 col-md-6 mb-5 mb-lg-0">
            <span class="service-icon rounded-circle mx-auto mb-3">
              <a class="service-icon rounded-circle mx-auto mb-3 js-scroll-trigger" href="#units">U</a>
            </span>
            <h4>
              <strong>Units Converter</strong>
            </h4>
          </div>
          <div class="col-lg-3 col-md-6 mb-5 mb-md-0">
            <span class="service-icon rounded-circle mx-auto mb-3">
              <a class="service-icon rounded-circle mx-auto mb-3 js-scroll-trigger" href="#currency">C</a>
            </span>
            <h4>
              <strong>Currency Converter</strong>
            </h4>
          </div>
        </div>
      </div>
    </section>

    <!-- Callout -->
    <section class="callout" id="units">
      <div class="converter-wrapper">
  <h1>Unit Converter</h1>

  <form name="property_form">
    <span>
      <select class="select-property" name="the_menu" size=1 onChange="UpdateUnitMenu(this, document.form_A.unit_menu); UpdateUnitMenu(this, document.form_B.unit_menu)">
      </select>
    </span>
  </form>

  <div class="converter-side-a">
    <form name="form_A" onSubmit="return false">
      <input type="text" class="numbersonly" name="unit_input" maxlength="20" value="0" onKeyUp="CalculateUnit(document.form_A, document.form_B)">
      <span>
        <select name="unit_menu" onChange="CalculateUnit(document.form_B, document.form_A)">
        </select>
      </span>
    </form>
  </div> <!-- /converter-side-a -->
  
 <div class="converter-equals">
   <p>=</p>
 </div> <!-- /converter-side-a -->

  <div class="converter-side-b">
    <form name="form_B" onSubmit="return false">
      <input type="text" class="numbersonly" name="unit_input" maxlength="20" value="0" onkeyup="CalculateUnit(document.form_B, document.form_A)">
      <span>
        <select name="unit_menu" onChange="CalculateUnit(document.form_A, document.form_B)">
        </select>
      </span>
    </form>
  </div> <!-- /converter-side-b -->
</div><!-- /converter-wrapper -->
    </section>

        <!-- Callout -->
    <section class="callout" id="currency">
      <div class="container text-center">
        <h1 class="">Currency
          converter</h1>
          <form name="converter">
          	<table border="0" align="center">
          		<tr>
          			<td style="color: #ffff" bgcolor="#263648">Euro: </td><td><input type="text" name="euro" onChange="euroConverter()" /></td>
          		</tr>
          		<tr>
          			<td style="color: #ffff" bgcolor="#263648">US Dollar: </td><td><input type="text" name="dollar" onChange="dollarConverter()" /></td>
          		</tr>
          		<tr>
          			<td style="color: #ffff" bgcolor="#263648">British Pound:</td><td><input type="text" name="pound" onChange="poundConverter()" /></td>
          		</tr>
          		<tr>
          			<td style="color: #ffff" bgcolor="#263648">Japanese Yen: </td><td><input type="text" name="yen" onChange="yenConverter()" /></td>
          		</tr>
          		<tr>
          			<td style="color: #ffff" bgcolor="#263648">PKR: </td><td><input type="text" name="pkr" onChange="pkrConverter()" /></td>
          		</tr>
          		<tr>
          			<td colspan="2" align="center"><input type="button" value="Convert!" /></td>
          		</tr>
          	</table>
          </form>
      </div>
    </section>


    <!-- Portfolio -->
    <section class="content-section bg-light" id="portfolio">
      <div class="container">
        <div class="content-section-heading text-center">
          <h2 class="mb-5">Thank you for using Cunverto</h2>
        </div>
       

    <!-- Footer -->
    <footer class="footer text-center">
      <div class="container">
        <p class="text-muted small mb-0">Copyright &copy; Your Website 2018</p>
      </div>
    </footer>

  </body>
<script src="js/unit.js"></script>
<script src="js/currency.js"></script>
</html>


'''



def homepage():
    # Create or overwrite the output file
    output_file = open('homepage.html', 'w')

      # Output the file
    output_file.write(main_page_head)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

homepage()
    

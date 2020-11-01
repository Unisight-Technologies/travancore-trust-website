var myCounter = 0;




  $(document).ready(function() {

      /* Every time the window is scrolled ... */
      $(window).scroll( function(){

          /* Check the location of each desired element */
          $('#counter').each( function(i){

              var bottom_of_object = $(this).position().top + $(this).outerHeight();
              var bottom_of_window = $(window).scrollTop() + $(window).height();

              /* If the object is completely visible in the window, fade it in */
              if( bottom_of_window > bottom_of_object ){

                  myCounter++;
                  if(myCounter == 1){
                    var num1 = 0;
                    var num2 = 0;
                    var num3 = 0;
                    var counter1 = 0;
                    var counter2 = 0;
                    var counter3 = 0;

                    var elem1 = document.getElementById("updateNum1");
                    setInterval(change1, 500);

                    function change1() {
                      if (num1 <= 5) {
                        elem1.innerHTML = num1.toString();
                        num1++;
                        counter1 = 0;
                      }
                    }

                    var elem2 = document.getElementById("updateNum2");
                    setInterval(change2, 50);

                    function change2() {
                      if (num2 <= 103) {
                        elem2.innerHTML = num2.toString();
                        num2++;
                        counter2 = 0;
                      }
                    }

                    var elem3 = document.getElementById("updateNum3");
                    setInterval(change3, 50);

                    function change3() {
                      if (num3 <= 3) {
                        elem3.innerHTML = num3.toString();
                        num3++;
                        counter3 = 0;
                      }
                    }

                  }

              }

          });

      });

  });

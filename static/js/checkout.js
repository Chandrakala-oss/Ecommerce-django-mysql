$(document).ready(function() {
    $('.payWithRazorpay').click(function(e) {
        e.preventDefault();
        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();

        // Corrected the if condition
        if(fname === "" || lname === "" || email === "" || phone === "" || address === "" || city === "" || state === "" || country === "" || pincode === "") {
           
            swal("Alert!", "All fields are mandatory!", "warning");
            return false;
        } else {
            $.ajax({
               method: "GET",
               url: "/proceed-to-pay",
               success: function(response){
                //console.log(response)
                var options = {
                    "key": "rzp_test_oRfSzsSGPgUAwU", // Enter the Key ID generated from the Dashboard
                    "amount": response.total_price, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "learning newthings ", //your business name
                    "description": "thank you for buying with us ",
                    "image": "https://example.com/your_logo",
                    //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the id obtained in the response of Step 1
                    "handler": function (response){
                        alert(response.razorpay_payment_id);
                        //alert(response.razorpay_order_id);
                        //alert(response.razorpay_signature)
                    },
                    "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                        "name": fname+" "+lname, //your customer's name
                        "email": email, 
                        "contact": phone //Provide the customer's phone number for better conversion rates 
                    },
                   /* "notes": {
                        "address": "Razorpay Corporate Office"
                    },*/
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
               
                rzp1.open();
               }
            })
            
           
        }
    })
});

       

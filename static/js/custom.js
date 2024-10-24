$('document').ready(function(){
    $('.increment-btn').click(function(e){
        e.preventDefault();
        var inc_value=$(this).closest('.product_data').find('.qty-input').val();
        var value =parseInt(inc_value,10);
        value=isNaN(value)?0:value;
        if(value<10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value)
        }
    })

    $('.decrement-btn').click(function(e){
        e.preventDefault();
        var dec_value=$(this).closest('.product_data').find('.qty-input').val();
        var value =parseInt(dec_value,10);
        value=isNaN(value)?0:value;
        if(value>1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value)
        }
    })
    $('.addToCartBtn').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            dataType: "json",  // Change this to "json" if expecting JSON
            success: function(response) {
                console.log(response);
                alertify.success(response.status);  // Ensure 'response.status' exists
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
                alertify.error("An error occurred: " + error);  // Handle errors
            }
        });
    });
     $('.addToWishlist').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                
                'csrfmiddlewaretoken': token
            },
             // Change this to "json" if expecting JSON
            success: function(response) {
                console.log(response);
                alertify.success(response.status);  // Ensure 'response.status' exists
            },

    });
});
    $('.changeQuantity').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name="csrfmiddlewaretoken"]').val();
        
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': token
            },
            dataType: "json",  // Change this to "json" if expecting JSON
            success: function(response) {
                console.log(response);
                alertify.success(response.status);  // Ensure 'response.status' exists
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
                alertify.error("An error occurred: " + error);  // Handle errors
            }
        });
    });

    $(document).on('click', '.delete-cart-item', function (e) {
        e.preventDefault();
    
        var $productData = $(this).closest('.product_data');
        var product_id = $productData.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                // Remove the product from the DOM
                $productData.remove();
                if ($('.product_data').length === 0) {
                    // If no items left, display empty cart message
                    $('.cartdata').html('<p>Your cart is empty.</p>');
                }
            },
            error: function (xhr, status, error) {
                alertify.error("Error deleting item. Please try again.");
            }
        });
    });
    $(document).on('click', '.delete-wishlist-item', function (e) {
        e.preventDefault();
    
        var $productData = $(this).closest('.product_data');
        var product_id = $productData.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                // Remove the product from the DOM
                $productData.remove();
                if ($('.product_data').length === 0) {
                    // If no items left, display empty cart message
                    $('.wishdata').html('<p>Your Wishlist is empty.</p>');
                }
            },
            error: function (xhr, status, error) {
                alertify.error("Error deleting item. Please try again.");
            }
        });
    });
 })


$(document).ready(function() {
    $('.view-btn').on('click', function() {
        var productId = $(this).data('product-id');  // Get the product ID from the button

        // Perform the AJAX request to get product details
        $.ajax({
            url: `/product/${productId}/`,  // Ensure this URL matches your Django routing, use backticks for template literals
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                // Check if data is returned correctly
                console.log("Data received:", data);  // Log the data for debugging

                // Ensure 'data' is valid before accessing properties
                if (data && !data.error) {
                    $('#modal-product-image').attr('src', data.imageURL || '');  // Set image URL
                    $('#modal-product-name').text(data.name || '');  // Set product name
                    $('#modal-product-price').text('৳' + (data.price ? data.price.toFixed(2) : '0.00'));  // Set product price
                    $('#productModal').modal('show');  // Show the modal
                } else {
                    console.error("Error in data:", data.error || "Unknown error");
                    alert('Failed to load product details.');
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX error:", error);  // Log any AJAX errors
                alert('An error occurred while fetching product details. Please try again later.');
            }
        });
    });
});

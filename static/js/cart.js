var updateButtons = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        if(user == 'AnonymousUser') {
            location.replace("/accounts/login/");
        }
        else{
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log({
                "productId": productId,
                "action": action,
            });
            updateCart(productId, action);
        }
    })
}

function updateCart(productId, action){
    console.log('updating cart...')

    var url = '/shop/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
    .then((response) => {
        console.log(response)
        return response.json()
    })
    .then((data) => {
        console.log("Data:", data)
        location.reload()
    })

}
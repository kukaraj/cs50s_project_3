var crust;
var size;
var topping;
var cart = false;

document.addEventListener('DOMContentLoaded',function(){

	document.querySelectorAll('.dropdown-menu li a').forEach( link => {

		link.onclick = function() {

			const name = this.innerText
			this.parentElement.parentElement.previousElementSibling.innerText = name;
			check_field(cart);
			return false;
		}

	});

	

    document.querySelector('.add_to_cart').onclick = ()=>{

    	cart = true;
    	check_field(cart)
    }

    document.querySelectorAll('.navbar .nav-link').forEach(function(link) {
    		if (link == window.location.href)
    			link.parentElement.classList.add('active')
    	});

    document.querySelector('#toppings_type').onclick = (event)=>{

		var name = event.target.innerText
		var blank = document.querySelector('.toppings').children[0]
		if (name == "1 topping"){
			blank.children[2].style.visibility = "visible"		
		}

		else if (name == "2 toppings"){
			blank.children[2].style.visibility = "visible"
			blank.children[3].style.visibility = "visible"
		}

		else if (name == "3 toppings"){
			blank.children[2].style.visibility = "visible"
			blank.children[3].style.visibility = "visible"
			blank.children[4].style.visibility = "visible"			
		}

		else{
			blank.children[2].style.visibility = "hidden"
			blank.children[3].style.visibility = "hidden"
			blank.children[4].style.visibility = "hidden"		
		}

		
    };




});

function check_field(cart){

	crust = document.querySelectorAll('.btn')[0].innerText
	size = document.querySelectorAll('.btn')[1].innerText
	topping = document.querySelectorAll('.btn')[2].innerText

	if (crust=='_ _ _ _ _ _ '){
		document.querySelector('.total_msg').innerHTML = "Please select a prefered pizza type"
	}

	else if(size=='_ _ _ _ _ _ '){
		document.querySelector('.total_msg').innerHTML = "Please select a prefered pizza size"
	}

	else if(topping=='_ _ _ _ _ _ '){
		document.querySelector('.total_msg').innerHTML = "Please select the prefered toppings"
	}

	else{
		document.querySelector('.total_msg').innerHTML = " "
		
		const price = new XMLHttpRequest();
		price.open('POST', '/order/price');
			price.onload = () => {
				const response = JSON.parse(price.responseText);
				document.querySelector('.total_value').innerHTML = response.price
				document.querySelector('.total_basket_value').innerHTML = response.total_price
			};

			var el = document.getElementsByName("csrfmiddlewaretoken");
			csrf_value = el[0].getAttribute("value");

			const data = new FormData();

			data.append('menu', "pizza");
		    data.append('data1', crust);
            data.append('data2', size);
            data.append('data3', topping);
            data.append('csrfmiddlewaretoken',csrf_value)

            if (cart){
            	data.append('cart',true)
            }

            price.send(data);
	}


}



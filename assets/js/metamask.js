async function connect(){
	if (typeof window.ethereum!=="undefined"){
	await window.ethereum.request ({method:"eth_requestAccounts"})
	window.location.href = 'https://www.youtube.com/watch?v=2zNSgSzhBfM&list=RDERTJj1uU8Xk&index=2';  
	}
	else {
        window.location.href = 'https://www.youtube.com/watch?v=2zNSgSzhBfM&list=RDERTJj1uU8Xk&index=2';
    }
}

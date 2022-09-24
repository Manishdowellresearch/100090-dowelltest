/*
window.onload = () => {
        fetch('https://100069.pythonanywhere.com/chat/get-rooms/', 
                             {method:'GET',
                              headers: {
                              'Accept': 'application/json',
                              'content-type':'application/json'}, 
                             //mode:'no-cors'
                             })
    .then(res => res.json())
    .then(data =>{console.log(data['Rooms'][0]['room_name'])})
    .catch(error => {console.log(error)})};
*/
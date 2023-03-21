const get_name = (evnt) => {
    evnt.preventDefault();
    evnt.stopPropagation();
    usr = document.getElementById('name-inp').value;
    console.log(usr);
    fetch(`/name=${usr}`).then((res) => {
        console.log(res, usr);
    })
};

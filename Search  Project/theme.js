document.getElementById('btn-toggle').addEventListener('click',()=>{
    if (document.body.classList.contains('dark')) {
        document.body.classList.remove('dark')
    }
    else {
        document.body.classList.add('dark')
    }
    document.getElementById('darkTheme').innerText = document.body.classList
})
main.js
async function switchpage(page) {
    m1 = document.getElementById('m1')
    m2 = document.getElementById('m2')
    p1 = document.getElementById('p1')
   

    if (page == 'main'){
        document.getElementById('m1').hidden = false
        document.getElementById('m2').hidden = true
        document.getElementById('p1').hidden = false
        document.getElementById('p2').hidden = true

        document.getElementById('m0').classList.add('active')
        document.getElementById('p0').classList.remove('active')

        swup.navigate('index.html');
        return
    }

    if (page == 'portfolio'){
        document.getElementById('m1').hidden = true
        document.getElementById('m2').hidden = false
        document.getElementById('p1').hidden = true
        document.getElementById('p2').hidden = false

        document.getElementById('m0').classList.remove('active')
        document.getElementById('p0').classList.add('active')

        swup.navigate('portfolio.html');
        return
    }
}
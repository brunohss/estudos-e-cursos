function contar(){
    let ini = document.getElementById('txti')
    let fim = document.getElementById('txtf')
    let passo = document.getElementById('txtp')
    let res = document.getElementById('res')

    if(ini.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        res.innerHTML +=`Impossivel Contar`
        window.alert('[ERROR] Falta dados! ')
    } else{
        res.innerHTML = 'Contando:'

        let i = Number(ini.value)
        let f = Number(fim.value)
        let p = Number(passo.value)
        if(p==0){res.innerHTML +=`Impossivel Contar`}

        if(i<f||(p<0 && i>f)){  
            if(p<0){p*=-1}

        for(let c = i; c<=f;c+=p){

            res.innerHTML +=`${c} \u{1F4A8}	`
            
        }
        

        }else{
    
                        
        for(let c = i; c>=f;c-=p){
            res.innerHTML +=`${c} \u{1F4A8}	`
            
        }

        }
        res.innerHTML +=`\u{1F3C1}	`





    }
}
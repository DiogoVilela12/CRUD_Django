(function(win, doc){
    'use strict';

    //VERIFICA SE O USUARIO QUER DELETAR O DADO
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('DESEJA APAGAR ESSE DADO PERMANENTEMENTE ?')){
                    return true
                }else{
                    event.preventDefault();
                }
            });
        }
    }

})(window,document);
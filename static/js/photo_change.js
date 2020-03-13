var r = document.getElementsByClassName('radius');
var photo = document.getElementsByClassName('change_photo');
var pre = document.getElementsByClassName('left_bracket');
var after = document.getElementsByClassName('right_bracket');

var index=1;

setInterval(changeImg,3000);

function changeImg(){
    index++;

    for(var j=0;j<4;j++){
        r[j].style.background = 'rgba(122,176,56,0)';
    }
    r[index-1].style.background = 'rgba(122,176,56,0.5)';
    if(index===1){
        photo[0].style.background = 'url("../static/img/homepage/当归饮片.jpg") 50% 50% / auto 100%';
    }
    else if(index===2){
        photo[0].style.background = 'url("../static/img/homepage/黄芪饮片.jpg") 50% 50% / auto 100% ';
    }
    else if(index===3){
        photo[0].style.background = 'url("../static/img/homepage/人参饮片.jpg") 50% 50% / auto 100%';
    }
    else{
        photo[0].style.background = 'url("../static/img/homepage/陈皮饮片.jpg") 50% 50% / auto 100%';
    }

    if(index===4){
        index=0;
    }
}



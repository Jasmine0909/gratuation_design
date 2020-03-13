var r = document.getElementsByClassName('radius');
var photo = document.getElementsByClassName('photo');
var index=0;

//改变图片
function ChangeImg() {
    index++;
    if(index>=photo.length) index=0;

    for(var i=0;i<photo.length;i++){
        photo[i].style.display='none';
        r[i].style.background = 'rgba(122,176,56,0)';
    }
    photo[index].style.display='block';
    r[index].style.background = 'rgba(122,176,56,0.5)';
}


// if(r[0].onclick()){
//     index = -1;
//     ChangeImg();
// }
// else if(r[1].onclick()){
//     index = 0;
//     ChangeImg();
// }
// else if(r[2].onclick()){
//     index = 1;
//     ChangeImg();
// }
// else if(r[3].onclick()){
//     index = 2;
//     ChangeImg();
// }
// //设置定时器，每隔两秒切换一张图片
// else{
//     setInterval(ChangeImg,3000);
// }
setInterval(ChangeImg,3000);

// var r = document.getElementsByClassName('radius')[1].onclick();
// r[1].style.background = 'rgba(122,176,56,0.5)';
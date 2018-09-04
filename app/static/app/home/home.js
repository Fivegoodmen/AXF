function aa() {
    //创建ajax对象xml请求
    if(window.XMLHttpRequest){
        var htx = new XMLHttpRequest();
    }else{
        var htx = new ActiveXObject('Microsoft.XMLHTTP');
    }
    //第二步 确定请求方式 地址 同步/异步
    htx.open('get','ajax.txt',true);
    //第三部 发送数据到服务器
    htx.onreadystatechange = function () {
        if(htx.readyState == 4 && htx.status == 200){
            alert(htx.responsseText);
            $.each(msg.lunbo, function (j,y) {
                $(".swiper-wrapper").append($('<div class="swiper-slide"><<img src=img/'+y.src+'/></div>div'>))

            });
        }

    }

}



// $(function () {
//     //启动顶部菜单轮播
//     initSwiper()
// //    启动必买轮播
//     initMustBuySwiper()
//
// })
//
// function initSwiper() {
//    var mySwiper = new Swiper ('#topSwiper', {
//     autoplay: 5000,//可选选项，自动滑动
//     loop: true,
//     // 如果需要分页器
//     pagination: '.swiper-pagination',
//
//   })
// }
//
//
// function initMustBuySwiper() {
//    var mySwiper = new Swiper ('#swiperMenu', {
//     slidesPerView: 3,  //一页显示的数量
//     spaceBetween: 5,  //每页之间的间隔
//   })
// }




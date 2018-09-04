// $(document).ready(function(){
//     document.documentElement.style.fontSize = innerWidth / 10 + "px";
// })
$(function () {
    alert(xxxxooooo到此一游)
    //加载数据
    $.ajax({
        url:'/static/HTML/home/',
        type:'GET',
        success:function (data) {
            //添加页码
            var prev = '<button value="prev">上页</button>';
            var next = '<button value="next">下页</button>';
            $('#page').append(prev)
            for (var j = 1;j <= data.pages; j++){
                var page = '<button value="'+j+'">'+j+'</button>';
                $('#page').append(page);
            }
            $('#page').append(next);
        }
        });
    //实现根据页码跳转页面
    $('#page').on('click','button',function () {

        var page = $(this).val();
        $.ajax({
            url:'/static/HTML/home/'
            type:'PUT',
            data:{
                'page':page
            },
            success: function (data) {
                if (data.code == 200){
                    window.location.href='base.html'
                }
            }
        })

    })

})
$(function(){
//	alert(1);  
    //用户查询
//  $("#sbtusersearch").click(function(){
////	  	alert(1);
//	  	vimsi = $("#searchimsi").val();
//		if($("#searchimsi").val()){
//		    $("#callimsi1").val(vimsi) ;
//		    $("#callimsi2").val(vimsi) ;
//	   };
//  });

	//公用部分
    $(document).click(function(){
    	if(flag == 1){
    		$(".searchprovresult").stop();
    		$(".searchprovresult").hide();
	    	flag = 0
    	};
    });
	
	//用户号码搜索框 & 搜索结果
    var flag = 0;	
    $("#searchprov").focusin(function(){
    	if(flag == 0){
	    	$(".searchprovresult").stop();
	    	$(".searchprovresult").show().animate({"height":"156px"});
	    	flag = 2
    	};
    	
    });
  	
    $("#searchprov").focusout(function(){
    	if(flag == 2){
    		$(".searchprovresult").stop();
//	    	$(".searchprovresult").hide();
	    	flag = 1
    	}
    });
  	
});

//导航
//$(".cm-top a").click(function(){
//	var num = $(this).index();
//	var va = $(".cm-top a");
//	va.eq(num).css({"color":"#1ABC9C","borderBottom":"1px solid #1ABC9C"});  		
//});

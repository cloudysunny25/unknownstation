/*var searchbar = document.querySelector("#keyword");
var searchbar2 = document.querySelector("#keyword2");
searchbar.style.opacity="0";
searchbar2.style.opacity="0";
searchbar2.style.height="0";
*/
//desktop 기준
var mql = window.matchMedia("only screen and (min-width:768px) and (orientation:landscape)");
/*
var searchbarBtn = document.getElementById("searchbarBtn");
*/
var search=false;
searchbarBtn.addEventListener("click",function(){
  var bar = document.getElementById("keyword2");
  if(search){
    bar.style.height="0px";
    bar.style.opacity="0";
    search=false;
  }else{
    bar.style.height="25px";
    bar.style.opacity="1";
    bar.placeholder=" search"
    search=true;
  }

})
/*
  if(mql.matches){
    searchbar2.style.opacity="0";
    searchbar2.style.height="0";
    if(!flag){
      searchbar.style.opacity="1";
      flag=true;
    }else{
      searchbar.style.opacity="0";
      flag=false;
    }
  }else{
    searchbar.style.opacity="0";
    if(!flag){
      searchbar2.style.opacity="1";
      searchbar2.style.height="auto";
      flag=true;
    }else{
      searchbar2.style.opacity="0";
      searchbar2.style.height="0";
      flag=false;
    }
  }
});
*/

function getURL(){
  var url = document.location.href.split("/");
  return url[0]+"/"+url[1]+"/"+url[2]+"/"+url[3]+"/";
}

function enter(){
  var keyword = "";

 if(mql.matches){
    keyword = document.getElementById("keyword").value;
  }else{
    keyword = document.getElementById("keyword2").value;
  }

  if(window.event.keyCode == 13){
      location.href=getURL()+"search?keyword="+keyword+"&page=1";
  }
}




//markdown editor
var btn = document.querySelector("#tabchange");
if(btn){
  var space1 = document.querySelector("#content");
  var space2 = document.querySelector("#markdown");
  space2.style.display="none";

  btn.addEventListener("click", function(){
   if(this.value=="preview"){
      checkMarkdownPreview();
      space1.style.display="none";
      space2.style.display="";
      this.value="editor";
    }else{
      space1.style.display="";
      space2.style.display="none";
      this.value="preview";
    }
  })

  var submit = false;
    function checkMarkdownPreview(){
      var text = {"text":document.querySelector(".content_write").value, "mode":"gfm"}
      var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       document.getElementById("markdown").innerHTML = this.responseText;
       document.getElementById("content_markdown").value = this.responseText;
       //alert(this.responseText)
       if(submit){
         var form = document.getElementById("write_form");
         form.submit();
       }
      }
    };

    xhttp.open("POST", "https://api.github.com/markdown", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.setRequestHeader('Authorization', 'bcbbe3360c392890e92034f22b21f182ba067be6');
    xhttp.send(JSON.stringify(text));
  }


  function write_form_submit(){
    //markdown 최종 결과를 한번더 받아온 뒤 제출
    submit = true;
    checkMarkdownPreview();
  }
}


function deletePost(){
    if(confirm("Do you really want to delete this post?")){
        document.getElementById("deleteForm").submit();
    }

  }
function resizeTextarea(obj){
    obj.style.height = "1px";
    obj.style.height = (12+obj.scrollHeight)+"px";
}

if(document.getElementById("content")){
  document.getElementById("content").addEventListener("keydown", function(e){
    this.style.height = "1px";
    this.style.height = (12+this.scrollHeight)+"px";
    if(e.keyCode === 9) { // tab was pressed
         // get caret position/selection
         var start = this.selectionStart;
         var end = this.selectionEnd;

         var target = e.target;
         var value = target.value;

         // set textarea value to: text before caret + tab + text after caret
         target.value = value.substring(0, start)
                     + "\t"
                     + value.substring(end);

         // put caret at right position again (add one for the tab)
         this.selectionStart = this.selectionEnd = start + 1;

         // prevent the focus lose
         e.preventDefault();
     }

  })

}

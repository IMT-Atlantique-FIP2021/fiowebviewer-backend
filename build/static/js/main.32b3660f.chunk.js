(this["webpackJsonpfiowebviewer-frontend"]=this["webpackJsonpfiowebviewer-frontend"]||[]).push([[0],{171:function(e){e.exports=JSON.parse('[{"name":0,"uv":4000,"pv":2400,"amt":2400,"average":800},{"name":1,"uv":3000,"pv":1398,"amt":2210,"average":300},{"name":2,"uv":2000,"pv":9800,"amt":2290,"average":945},{"name":3,"uv":2780,"pv":3908,"amt":2000,"average":1450},{"name":4,"uv":1890,"pv":4800,"amt":2181,"average":289},{"name":5,"uv":2390,"pv":3800,"amt":2500,"average":789},{"name":6,"uv":3490,"pv":4300,"amt":2100,"average":987},{"name":7,"uv":3490,"pv":4300,"amt":2100,"average":987},{"name":8,"uv":3490,"pv":4300,"amt":2100,"average":987},{"name":9,"uv":3490,"pv":4300,"amt":2100,"average":987},{"name":10,"uv":3490,"pv":4300,"amt":2100,"average":987}]')},202:function(e,t,s){},343:function(e,t,s){"use strict";s.r(t);var i=s(0),a=s.n(i),n=s(56),c=s.n(n),r=(s(202),s(25)),l=s.p+"static/media/logo.6904a498.svg",d=s(1);function o(){return Object(d.jsx)("div",{id:"HEADER",className:"bg-blue-ovh-dark py-7",children:Object(d.jsx)("div",{className:"container mx-auto px-5",children:Object(d.jsx)("div",{className:"flex flex-row justify-between",children:Object(d.jsxs)(r.b,{to:"/",className:"flex items-center text-white group",children:[Object(d.jsx)("img",{src:l,className:"transition duration-1000 ease-in-out transform group-hover:-rotate-180 h-7",alt:""}),Object(d.jsx)("div",{className:"font-bold text-2xl ml-1 mr-3",children:"FLEX"}),Object(d.jsx)("div",{className:"font-light text-xl opacity-80 group-hover:opacity-100",children:"Flexible I/O Explorer"})]})})})})}var b=s(345),j=s(346),x=s(347);function h(){return Object(d.jsx)("div",{id:"NAVBAR",className:"bg-blue-ovh-light",children:Object(d.jsx)("div",{className:"container mx-auto",children:Object(d.jsxs)("div",{className:"flex flex-row",children:[Object(d.jsx)(r.b,{to:"/",children:Object(d.jsx)(u,{icon:b.a,text:"Result Table"})}),Object(d.jsx)(r.b,{to:"/download",children:Object(d.jsx)(u,{icon:j.a,text:"Download Script"})}),Object(d.jsx)("div",{className:"flex-grow"}),Object(d.jsx)(r.b,{to:"/docs",children:Object(d.jsx)(u,{icon:x.a,text:"Docs"})})]})})})}function u(e){return Object(d.jsx)("div",{className:"px-5",children:Object(d.jsx)("div",{className:"text-white font-semibold py-4 opacity-70 hover:opacity-100 hover:border-gray-200 border-blue-ovh-light border-b-2",children:Object(d.jsxs)("div",{className:"flex flex-row items-center",children:[Object(d.jsx)(e.icon,{className:"mr-1 h-5"}),e.text]})})})}var m=s(16),v=s(27),O=s.n(v),p=s(29),f=s(80),g=s(70),y=s(71),N=s(72),w=s(79),_=s(348),k=s(349),L=s(350),C=s(351),M=s(352),E=function(e){Object(N.a)(s,e);var t=Object(w.a)(s);function s(e){var i;return Object(g.a)(this,s),(i=t.call(this,e)).state=void 0,i.timer=void 0,i.state={loading:!0,fetching:!1,results:[]},i.timer=null,i}return Object(y.a)(s,[{key:"getCurrentResultSelectedState",value:function(e){var t;return(null===(t=this.state.results.filter((function(t){return t.id===e}))[0])||void 0===t?void 0:t.selected)||!1}},{key:"fetchResults",value:function(){var e=Object(f.a)(O.a.mark((function e(){var t,s,i,a=this;return O.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!this.state.fetching){e.next=4;break}return e.abrupt("return");case 4:this.setState(Object(p.a)(Object(p.a)({},this.state),{},{isFetching:!0}));case 5:return"/api/result/",e.next=8,fetch("/api/result/");case 8:return t=e.sent,e.next=11,t.json();case 11:s=e.sent,i=s.map((function(e){return{id:e.id,name:e.name,tags:e.tags,submitted_at:e.time,selected:a.getCurrentResultSelectedState(e.id)}})),this.setState({loading:!1,isFetching:!1,results:i});case 14:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"componentDidMount",value:function(){var e=Object(f.a)(O.a.mark((function e(){var t=this;return O.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchResults();case 2:this.timer=setInterval((function(){return t.fetchResults()}),1e3);case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"componentWillUnmount",value:function(){this.timer&&(clearInterval(this.timer),this.timer=null)}},{key:"isAllSelected",value:function(){return this.state.results.filter((function(e){return e.selected})).length===this.state.results.length&&0!==this.state.results.length}},{key:"selectedResult",value:function(){return this.state.results.filter((function(e){return e.selected})).map((function(e){return e.id}))}},{key:"handleOnCheckbox_SelectAll",value:function(){var e=!this.isAllSelected();this.setState(this.state.results.map((function(t){return t.selected=e})))}},{key:"handleOnCheckbox_Select",value:function(e){var t=this.state.results.filter((function(t){return t.id===e})).map((function(e){return e.selected=!e.selected}));this.setState(t)}},{key:"handleOnDeleteClick",value:function(){var e=Object(f.a)(O.a.mark((function e(t){return O.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return"/api/result/",e.next=3,fetch("/api/result/"+t,{method:"DELETE"});case 3:this.fetchResults();case 4:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"handleOnDeleteSelectedClick",value:function(){var e=Object(f.a)(O.a.mark((function e(){return O.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:"/api/result/",this.selectedResult().forEach((function(e){fetch("/api/result/"+e,{method:"DELETE"})})),this.fetchResults();case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e,t=this,s=this.state.results;return Object(d.jsxs)("div",{children:[Object(d.jsxs)("table",{className:"table-fixed w-full",children:[(e={checked:this.isAllSelected(),onChange:this.handleOnCheckbox_SelectAll.bind(this)},Object(d.jsx)("thead",{children:Object(d.jsxs)("tr",{className:"text-left border-b",children:[Object(d.jsx)("th",{className:"w-14",children:Object(d.jsx)("div",{className:"flex content-center justify-center",children:Object(d.jsx)("input",Object(p.a)(Object(p.a)({},e),{},{type:"checkbox",className:"rounded"}))})}),Object(d.jsx)("th",{className:"py-4 px-4 w-64",children:"Job Name"}),Object(d.jsx)("th",{className:"py-4 px-4",children:"Tags"}),Object(d.jsx)("th",{className:"py-4 w-32 text-center",children:"Submitted at"}),Object(d.jsx)("th",{className:"w-20 text-center"})]})})),Object(d.jsx)("tbody",{children:s.map((function(e){return Object(d.jsx)(F,{result:e,checkbox:{checked:e.selected,onChange:t.handleOnCheckbox_Select.bind(t,e.id)},actions:{onDeleteClick:t.handleOnDeleteClick.bind(t,e.id)}},e.id)}))})]}),T(this.state.loading,this.state.results,this.selectedResult(),this.handleOnDeleteSelectedClick.bind(this))]})}}]),s}(i.Component);function T(e,t,s,i){return e?Object(d.jsxs)("div",{className:"flex flex-row justify-center p-4 animate-pulse",children:[Object(d.jsx)(_.a,{className:"animate-spin mr-4"}),Object(d.jsx)("div",{className:"select-none",children:"Fetching results..."})]}):0===t.length?Object(d.jsxs)("div",{className:"flex flex-row justify-center p-4 opacity-70",children:[Object(d.jsx)(k.a,{className:"mr-4"}),Object(d.jsx)("div",{className:"select-none",children:"No result available..."})]}):t?Object(d.jsxs)("div",{className:"flex justify-evenly p-4",children:[R(s),B(s,i)]}):void 0}function F(e){return Object(d.jsxs)("tr",{className:"border-b odd:bg-gray-100",children:[S(e.result.id,e.checkbox),(s=e.result.name,i=e.result.id,Object(d.jsx)("td",{className:"px-4 truncate",children:Object(d.jsx)(r.b,{to:{pathname:"/result",search:"?id="+i},className:"text-blue-ovh-light hover:text-blue-ovh-dark underline text-base",children:s})})),D(e.result.tags),(t=e.result.submitted_at,Object(d.jsx)("td",{className:"px-4 text-xs text-center",children:t})),I(e.actions)]});var t,s,i}function S(e,t){var s=Object(p.a)(Object(p.a)({},t),{},{id:"checkbox_"+e});return Object(d.jsx)("td",{children:Object(d.jsx)("div",{className:"flex content-center justify-center",children:Object(d.jsx)("input",Object(p.a)(Object(p.a)({},s),{},{type:"checkbox",className:"rounded"}))})})}function D(e){function t(e){return Object(d.jsxs)("div",{className:"flex flex-row flex-none bg-gray-300 rounded-full px-2 my-1 items-center",children:[Object(d.jsx)(L.a,{size:18,className:"pr-1"}),Object(d.jsx)("div",{className:"text-xs font-semibold",children:e})]})}return Object(d.jsx)("td",{className:"px-4",children:Object(d.jsx)("div",{className:"flex flex-row justify-start space-x-2 overflow-x-auto scrollbar-thin",children:e.map((function(e){return t(e)}))})})}function I(e){return Object(d.jsx)("td",{className:"px-4",children:Object(d.jsxs)("div",{className:"flex flex-row justify-start space-x-1",children:[Object(d.jsx)("button",{onClick:e.onDeleteClick,children:Object(d.jsx)(C.a,{size:20,className:"text-red-500"})}),Object(d.jsx)("button",{children:Object(d.jsx)(M.a,{size:20,className:"text-blue-500"})})]})})}function R(e){var t="?".concat(e.map((function(e){return"id="+e})).join("&"));return Object(d.jsx)(r.b,{to:{pathname:"/compare",search:t},children:Object(d.jsxs)("button",{disabled:e.length<=1,className:"disabled:opacity-50 disabled:bg-gray-400 bg-blue-ovh-light hover:opacity-100 opacity-80 p-2 w-64 font-semibold border rounded text-white",children:["Compare ",e.length," result",e.length>1?"s":""]})})}function B(e,t){return Object(d.jsxs)("button",{disabled:e.length<=0,onClick:t,className:"disabled:opacity-50 disabled:bg-gray-400 bg-red-600 hover:opacity-100 opacity-80 p-2 w-64 font-semibold border rounded text-white",children:["Delete ",e.length," result",e.length>1?"s":""]})}var V=s(93),P=s(353),A=s(354),W=s(362),z=s(355),G=s(359),J=s(190),Y=s(191),U=s(83),H=s(193),K=s(188),q=s(171),X=s(37),Q=s(209);function Z(){return Object(d.jsx)("div",{className:"px-5 py-3",children:Object(d.jsx)("div",{className:"container mx-auto px-5",children:Object(d.jsxs)("div",{className:"grid grid-cols-1 lg:grid-cols-2 lg:space-x-5",children:[Object(d.jsxs)("div",{className:"space-y-5",children:[Object(d.jsxs)($,{tableName:"FIO Test Name",open:!0,children:[Object(d.jsx)($,{tableName:"FIO user args",subMenu:!0,open:!0,children:Object(d.jsx)("div",{className:"px-5 text-xs",children:"./fio-webviewer.sh --webviewer-tag FIO-READ-WRITE --webviewer-name FIO-TESTRW --name=randwrite --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=2 --runtime=240 --output=~/fioviewer/test.txt"})}),Object(d.jsx)($,{tableName:"Output",subMenu:!0,open:!0,children:Object(d.jsx)("div",{"flex-none":!0,className:"px-5 text-xs ",children:"randread: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=psync, iodepth=16 ... fio-3.8 Starting 4 processes randread: Laying out IO file (1 file / 512MiB) randread: Laying out IO file (1 file / 512MiB) randread: Laying out IO file (1 file / 512MiB) randread: Laying out IO file (1 file / 512MiB)"})}),Object(d.jsx)($,{tableName:"CSV",subMenu:!0,open:!0,children:Object(d.jsx)("div",{"flex-none":!0,className:"px-5 text-s  text-blue-ovh-light underline hover:text-blue-ovh-dark ",children:Object(d.jsx)("a",{href:"https://guigui.io/",children:"Download all as tar.gz"})})})]}),Object(d.jsxs)($,{tableName:"READ",open:!0,children:[Object(d.jsx)($,{tableName:"OVERVIEW",subMenu:!0,open:!0,children:te(X,"read")}),Object(d.jsx)($,{tableName:"COMPLETION LATENCY PERCENTILE",subMenu:!0,open:!0,children:Object(d.jsx)(je,{testList:le,data:ae(X,"read"),xDatakey:"clat_percentile",xLabel:"%",yLabel:"ms",valueOnGraph:!0})})]}),Object(d.jsxs)($,{tableName:"WRITE",open:!0,children:[Object(d.jsx)($,{tableName:"OVERVIEW",subMenu:!0,open:!0,children:te(X,"write")}),Object(d.jsx)($,{tableName:"COMPLETION LATENCY PERCENTILE",subMenu:!0,open:!0,children:Object(d.jsx)(je,{testList:le,data:ae(X,"write"),xDatakey:"clat_percentile",xLabel:"%",yLabel:"ms",valueOnGraph:!0})})]}),Object(d.jsxs)($,{tableName:"TRIM",open:!0,children:[Object(d.jsx)($,{tableName:"OVERVIEW",subMenu:!0,open:!0,children:te(X,"trim")}),Object(d.jsx)($,{tableName:"COMPLETION LATENCY PERCENTILE",subMenu:!0,open:!0,children:Object(d.jsx)(je,{testList:le,data:ae(X,"trim"),xDatakey:"clat_percentile",xLabel:"%",yLabel:"ms",valueOnGraph:!0})})]}),Object(d.jsx)($,{tableName:"IO DEPTH",open:!0,children:Object(d.jsx)(je,{testList:oe,data:ne(X).filter((function(e){return 0!=e.value})),xDatakey:"io_depth",xLabel:"Depth Level",yLabel:"%",valueOnGraph:!0})}),Object(d.jsx)($,{tableName:"LATENCY",open:!0,children:Object(d.jsx)(je,{testList:de,data:ce(X).filter((function(e){return 0!=e.value})),xDatakey:"latency",xLabel:"ms",yLabel:"%",valueOnGraph:!0})}),Object(d.jsx)($,{tableName:"CPU",open:!0,children:se(X)})]}),Object(d.jsx)("div",{className:"space-y-5 py-5 lg:py-0",children:Object(d.jsx)($,{tableName:"Jobs",open:!0,children:Object(d.jsx)(be,{})})})]})})})}var $=function(e){Object(N.a)(s,e);var t=Object(w.a)(s);function s(e){var i;return Object(g.a)(this,s),(i=t.call(this,e)).state=void 0,i.subMenu=void 0,i.tableName=void 0,i.onVisibilityChange=i.onVisibilityChange.bind(Object(V.a)(i)),i.subMenu=e.subMenu||!1,i.state={isOpen:e.open||!1},i.tableName=e.tableName||"",i}return Object(y.a)(s,[{key:"onVisibilityChange",value:function(){this.setState({isOpen:!this.state.isOpen})}},{key:"render",value:function(){return this.subMenu?Object(d.jsxs)("div",{className:"py-1 border-b",children:[Object(d.jsx)("div",{children:ee(this.tableName,this.state.isOpen,this.onVisibilityChange)}),this.state.isOpen&&Object(d.jsx)("div",{children:this.props.children})]}):Object(d.jsxs)("div",{className:"flex-none rounded shadow-lg bg-white ",children:[Object(d.jsx)("div",{className:"bg-blue-ovh-light h-1 rounded-t"}),Object(d.jsx)("div",{className:"font-bold py-3 border-b",children:ee(this.tableName,this.state.isOpen,this.onVisibilityChange)}),this.state.isOpen&&Object(d.jsx)("div",{children:this.props.children})]})}}]),s}(i.Component);function ee(e,t,s){return Object(d.jsxs)("div",{className:"flex px-5",children:[Object(d.jsx)("button",{onClick:s,className:"align-bottom",children:t?Object(d.jsx)(P.a,{}):Object(d.jsx)(A.a,{})}),e]})}function te(e,t){var s=ae(e,t),i=e.jobs[0][t],a=(i.io_kbytes/1e3).toFixed(2)+"MB",n=(i.bw/1e3).toFixed(2)+"MB/s",c=i.iops.toFixed(2),r=Math.trunc(i.runtime/36e5)+"h "+Math.trunc(i.runtime/6e4%60)+"m "+(i.runtime/1e3%60).toFixed(0)+"s",l=i.slat_ns,o=i.clat_ns,b=i.lat_ns,j=(l.min/1e6).toFixed(3)+" ms",x=(l.max/1e6).toFixed(3)+" ms",h=(l.mean/1e6).toFixed(3)+" ms",u=(l.stddev/1e6).toFixed(3)+" ms",m=(o.min/1e6).toFixed(3)+" ms",v=(o.max/1e6).toFixed(3)+" ms",O=(o.mean/1e6).toFixed(3)+" ms",p=(o.stddev/1e6).toFixed(3)+" ms",f=(b.min/1e6).toFixed(3)+" ms",g=(b.max/1e6).toFixed(3)+" ms",y=(b.mean/1e6).toFixed(3)+" ms",N=(b.stddev/1e6).toFixed(3)+" ms",w=(i.bw_min/1e3).toFixed(2)+" MB/s",_=(i.bw_max/1e3).toFixed(2)+" MB/s",k=(i.bw_mean/1e3).toFixed(2)+" MB/s",L=(i.bw_dev/1e3).toFixed(2)+" MB/s",C=i.bw_agg.toFixed(2)+" %",M="grid grid-flow-col grid-cols-"+s.length+"grid-rows-2";return Object(d.jsxs)("div",{className:"",children:[Object(d.jsxs)("div",{className:"grid grid-flow-col grid-flow-row grid-cols-4 grid-rows-2 text-sm divide-y divide-x text-center",children:[Object(d.jsx)("div",{children:"Io"}),Object(d.jsx)("div",{children:a}),Object(d.jsx)("div",{children:"Bandwidth"}),Object(d.jsx)("div",{children:n}),Object(d.jsx)("div",{children:"Iops"}),Object(d.jsx)("div",{children:c}),Object(d.jsx)("div",{children:"Runtime"}),Object(d.jsx)("div",{children:r})]}),Object(d.jsxs)("div",{className:"p-2 grid grid-flow-col grid-flow-row grid-cols-5 grid-rows-4 text-sm  divide-y divide-x text-center",children:[Object(d.jsx)("div",{}),Object(d.jsx)("div",{children:"Submition Latency"}),Object(d.jsx)("div",{children:"Competion Latency"}),Object(d.jsx)("div",{children:"Latency"}),Object(d.jsx)("div",{children:"Min"}),Object(d.jsx)("div",{children:j}),Object(d.jsx)("div",{children:m}),Object(d.jsx)("div",{children:f}),Object(d.jsx)("div",{children:"Max"}),Object(d.jsx)("div",{children:x}),Object(d.jsx)("div",{children:v}),Object(d.jsx)("div",{children:g}),Object(d.jsx)("div",{children:"Mean"}),Object(d.jsx)("div",{children:h}),Object(d.jsx)("div",{children:O}),Object(d.jsx)("div",{children:y}),Object(d.jsx)("div",{children:"Standard Deviation"}),Object(d.jsx)("div",{children:u}),Object(d.jsx)("div",{children:p}),Object(d.jsx)("div",{children:N})]}),Object(d.jsx)("div",{className:"text-lg text-center",children:"Bandwidth"}),Object(d.jsxs)("div",{className:" grid grid-flow-col grid-flow-row grid-cols-5 grid-rows-2 text-sm divide-y divide-x text-center",children:[Object(d.jsx)("div",{children:"Min"}),Object(d.jsx)("div",{children:w}),Object(d.jsx)("div",{children:"Max"}),Object(d.jsx)("div",{children:_}),Object(d.jsx)("div",{children:"Mean"}),Object(d.jsx)("div",{children:k}),Object(d.jsx)("div",{children:"Standard Deviation"}),Object(d.jsx)("div",{children:L}),Object(d.jsx)("div",{children:"Percentage"}),Object(d.jsx)("div",{children:C})]}),Object(d.jsx)("div",{className:M})]})}function se(e){var t=e.jobs[0],s=t.usr_cpu+" %",i=t.sys_cpu+" %",a=t.ctx,n=t.majf,c=t.minf;return Object(d.jsx)("div",{children:Object(d.jsxs)("div",{className:"grid grid-flow-col grid-flow-row grid-cols-2 grid-rows-5 text-sm divide-y divide-x text-center",children:[Object(d.jsx)("div",{children:"User"}),Object(d.jsx)("div",{children:"System"}),Object(d.jsx)("div",{children:"Context Switches"}),Object(d.jsx)("div",{children:"Major Fault"}),Object(d.jsx)("div",{children:"Minor Fault"}),Object(d.jsx)("div",{children:s}),Object(d.jsx)("div",{children:i}),Object(d.jsx)("div",{children:a}),Object(d.jsx)("div",{children:n}),Object(d.jsx)("div",{children:c})]})})}function ie(){return Q({luminosity:"bright",hue:"random"})}function ae(e,t){var s=e.jobs[0][t].clat_ns.percentile,i=[];for(var a in s)i.push({clat_percentile:Number.parseFloat(a).toString(),value:s[a].toPrecision(3)/1e6});return i}function ne(e){var t=e.jobs[0].iodepth_level,s=[];for(var i in t)s.push({io_depth:i,value:t[i].toPrecision(3)});return s}function ce(e){var t=e.jobs[0].latency_us,s=e.jobs[0].latency_ms,i=[];for(var a in t)i.push({latency:+a/1e3,value:t[a].toPrecision(4)});for(var n in s)i.push({latency:+n,value:s[n].toPrecision(3)});return i}var re=[{id:"average",color:"blue",activated:!0},{id:"uv",color:ie(),activated:!0},{id:"pv",color:ie(),activated:!0},{id:"amt",color:ie(),activated:!0}],le=[{id:"value",color:"blue",activated:!0}],de=[{id:"value",color:"blue",activated:!0}],oe=[{id:"value",color:"blue",activated:!0}],be=function(e){Object(N.a)(s,e);var t=Object(w.a)(s);function s(e){var i;return Object(g.a)(this,s),(i=t.call(this,e)).state=void 0,i.state=i.initState(),i}return Object(y.a)(s,[{key:"initState",value:function(){return{data:q,activatedValue:re}}},{key:"handleOnChange",value:function(e){var t=this.state.activatedValue;t.filter((function(t){return t.id===e})).map((function(e){return e.activated=!e.activated})),this.setState(Object(p.a)(Object(p.a)({},this.state),{},{activatedValue:t}))}},{key:"render",value:function(){var e=this;return Object(d.jsxs)("div",{className:"grid grid-cols-4 auto-layout",children:[Object(d.jsx)("div",{className:"col-span-1 border-r-2 p-2",children:this.state.activatedValue.map((function(t){t.id;return Object(d.jsxs)("div",{children:[Object(d.jsx)("input",{id:t.id,checked:t.activated,type:"checkbox",className:"rounded ml-2 mr-2",onChange:e.handleOnChange.bind(e,t.id)}),Object(d.jsx)("label",{style:{color:t.color},htmlFor:t.id,children:t.id})]})}))}),Object(d.jsxs)("div",{className:"col-span-3",children:[Object(d.jsx)(je,{testList:this.state.activatedValue,data:this.state.data,xTickCount:this.state.data.length/10+2,xType:"number",xDatakey:"name",title:"Bandwidth",xLabel:"t[s]",yLabel:"MB/s"}),Object(d.jsx)(je,{testList:this.state.activatedValue,data:this.state.data,xTickCount:this.state.data.length/10+2,xType:"number",xDatakey:"name",title:"IOPS",xLabel:"t[s]",yLabel:"iops"}),Object(d.jsx)(je,{testList:this.state.activatedValue,data:this.state.data,xTickCount:this.state.data.length/10+2,xType:"number",xDatakey:"name",title:"Latency",xLabel:"t[s]",yLabel:"ms"}),Object(d.jsx)(je,{testList:this.state.activatedValue,data:this.state.data,xTickCount:this.state.data.length/10+2,xType:"number",xDatakey:"name",title:"Submission Latency",xLabel:"t[s]",yLabel:"ms"}),Object(d.jsx)(je,{testList:this.state.activatedValue,data:this.state.data,xTickCount:this.state.data.length/10+2,xType:"number",xDatakey:"name",title:"Completion Latency",xLabel:"t[s]",yLabel:"ms"}),Object(d.jsx)("div",{className:"p-5"})]})]})}}]),s}(i.Component);function je(e){var t=e.valueOnGraph||!1;return Object(d.jsxs)("div",{className:"h-60 p-5",children:[Object(d.jsx)("div",{className:"text-lg text-center",children:e.title}),Object(d.jsx)(W.a,{width:"100%",height:"100%",children:Object(d.jsxs)(z.a,{width:500,height:300,data:e.data,margin:{top:15,right:15,left:10,bottom:20},children:[Object(d.jsx)(G.a,{strokeDasharray:"3 3"}),Object(d.jsx)(J.a,{dataKey:e.xDatakey,type:e.xType||"category",tickCount:e.xTickCount||5,allowDecimals:!0,label:{value:e.xLabel,position:"bottom"}}),Object(d.jsx)(Y.a,{label:{value:e.yLabel,angle:-90,position:"left"}}),Object(d.jsx)(U.a,{}),e.testList.map((function(e){if(e.activated)return Object(d.jsx)(H.a,{type:"linear",dataKey:e.id,stroke:e.color,activeDot:{r:5},children:t?Object(d.jsx)(K.a,{dataKey:e.id,position:"top",offset:10,className:"text-xs"}):""})}))]})})]})}function xe(){return Object(d.jsx)("div",{className:"px-5 py-3",children:"Not Implemented Yet..."})}function he(){var e=new URLSearchParams(Object(m.f)().search);return Object(d.jsx)("div",{id:"CONTENT",className:"my-8 flex flex-col space-y-5",children:Object(d.jsxs)(m.c,{children:[Object(d.jsx)(m.a,{path:"/result",children:Object(d.jsx)(Z,{})}),Object(d.jsx)(m.a,{path:"/compare",children:Object(d.jsx)(ue,{title:"Compare "+e.getAll("id").join(" & ")||!1,children:Object(d.jsx)(xe,{})})}),Object(d.jsx)(m.a,{path:"/",children:Object(d.jsx)(ue,{title:"Result Table",children:Object(d.jsx)(E,{})})})]})})}function ue(e){return Object(d.jsx)("div",{className:"container mx-auto px-5",children:Object(d.jsxs)("div",{className:"rounded shadow-lg bg-white",children:[Object(d.jsx)("div",{className:"bg-blue-ovh-light h-1 rounded-t"}),Object(d.jsx)("div",{className:"px-5 py-3 border-b",children:Object(d.jsx)("div",{className:"text-xl",children:e.title})}),Object(d.jsx)("div",{children:e.children})]})})}var me=s(360);function ve(){return Object(d.jsx)("div",{id:"FOOTER",className:"bg-blue-ovh-light py-5",children:Object(d.jsx)("div",{className:"container mx-auto px-5",children:Object(d.jsxs)("div",{className:"flex flex-row justify-between",children:[Object(d.jsx)("div",{className:"text-white font-light",children:"OVHCloud \xa9 2021"}),Object(d.jsxs)("a",{href:"https://github.com/IMT-Atlantique-FIP2021/fiowebviewer-frontend",className:"text-white font-light hover:underline flex group",children:["Source code available on",Object(d.jsx)(me.a,{className:"ml-2 opacity-80 group-hover:opacity-100"})]})]})})})}var Oe=function(){return Object(d.jsxs)("div",{className:"flex flex-col min-h-screen",children:[Object(d.jsxs)("div",{className:"flex-auto bg-gray-200 dark:bg-gray-800",children:[Object(d.jsx)(o,{}),Object(d.jsx)(h,{}),Object(d.jsx)(he,{})]}),Object(d.jsx)(ve,{})]})};var pe=function(){return Object(d.jsx)(r.a,{children:Object(d.jsx)(Oe,{})})},fe=function(e){e&&e instanceof Function&&s.e(3).then(s.bind(null,363)).then((function(t){var s=t.getCLS,i=t.getFID,a=t.getFCP,n=t.getLCP,c=t.getTTFB;s(e),i(e),a(e),n(e),c(e)}))};c.a.render(Object(d.jsx)(a.a.StrictMode,{children:Object(d.jsx)(pe,{})}),document.getElementById("root")),fe()},37:function(e){e.exports=JSON.parse('{"fio version":"fio-3.16","timestamp":1614710871,"timestamp_ms":1614710871482,"time":"Tue Mar  2 19:47:51 2021","jobs":[{"jobname":"fio-test-1","groupid":0,"error":0,"eta":0,"elapsed":4,"job options":{"name":"fio-test-2","ioengine":"libaio","direct":"1","invalidate":"1","size":"10m","rw":"randrw","rwmixread":"40","randrepeat":"0","bssplit":"64k/47:4k/22:16k/12:8k/6:512/5:32k/4:12k/3:256k/1,8k/89:4k/11","iodepth":"32","runtime":"3"},"read":{"io_bytes":578833408,"io_kbytes":565267,"bw_bytes":192880175,"bw":188359,"iops":10115.961346,"runtime":79457778,"total_ios":30358,"short_ios":0,"drop_ios":0,"slat_ns":{"min":26517,"max":635097,"mean":38036.146024,"stddev":14619.087445},"clat_ns":{"min":34647,"max":5857659,"mean":1138115.210554,"stddev":393222.020597,"percentile":{"1.000000":296960,"5.000000":733184,"10.000000":864256,"20.000000":978944,"30.000000":1044480,"40.000000":1089536,"50.000000":1122304,"60.000000":1155072,"70.000000":1204224,"80.000000":1253376,"90.000000":1351680,"95.000000":1482752,"99.000000":2113536,"99.500000":4358144,"99.900000":5144576,"99.950000":5341184,"99.990000":5537792}},"lat_ns":{"min":65097,"max":5914265,"mean":1176575.360465,"stddev":396749.449709},"bw_min":178833,"bw_max":201263,"bw_agg":99.180076,"bw_mean":186814.6,"bw_dev":9295.709457,"bw_samples":5,"iops_min":9817,"iops_max":10461,"iops_mean":10077.2,"iops_stddev":243.102242,"iops_samples":5},"write":{"io_bytes":328583168,"io_kbytes":320882,"bw_bytes":109491225,"bw":106925,"iops":15064.978341,"runtime":3001,"total_ios":45210,"short_ios":0,"drop_ios":0,"slat_ns":{"min":27595,"max":740386,"mean":37346.795775,"stddev":22681.906364},"clat_ns":{"min":34155,"max":5927392,"mean":1324485.779451,"stddev":370522.404075,"percentile":{"1.000000":419840,"5.000000":1089536,"10.000000":1138688,"20.000000":1171456,"30.000000":1204224,"40.000000":1236992,"50.000000":1269760,"60.000000":1302528,"70.000000":1351680,"80.000000":1433600,"90.000000":1548288,"95.000000":1695744,"99.000000":2375680,"99.500000":4358144,"99.900000":5079040,"99.950000":5406720,"99.990000":5734400}},"lat_ns":{"min":66820,"max":6026544,"mean":1362254.725658,"stddev":383345.263246},"bw_min":104382,"bw_max":108383,"bw_agg":99.184101,"bw_mean":106052.6,"bw_dev":1723.16868,"bw_samples":5,"iops_min":14763,"iops_max":15323,"iops_mean":15015.2,"iops_stddev":237.25029,"iops_samples":5},"trim":{"io_bytes":0,"io_kbytes":0,"bw_bytes":0,"bw":0,"iops":0,"runtime":0,"total_ios":0,"short_ios":0,"drop_ios":0,"slat_ns":{"min":0,"max":0,"mean":0,"stddev":0},"clat_ns":{"min":0,"max":0,"mean":0,"stddev":0,"percentile":{"1.000000":0,"5.000000":0,"10.000000":0,"20.000000":0,"30.000000":0,"40.000000":0,"50.000000":0,"60.000000":0,"70.000000":0,"80.000000":0,"90.000000":0,"95.000000":0,"99.000000":0,"99.500000":0,"99.900000":0,"99.950000":0,"99.990000":0}},"lat_ns":{"min":0,"max":0,"mean":0,"stddev":0},"bw_min":0,"bw_max":0,"bw_agg":0,"bw_mean":0,"bw_dev":0,"bw_samples":0,"iops_min":0,"iops_max":0,"iops_mean":0,"iops_stddev":0,"iops_samples":0},"sync":{"lat_ns":{"min":0,"max":0,"mean":0,"stddev":0,"percentile":{"1.000000":0,"5.000000":0,"10.000000":0,"20.000000":0,"30.000000":0,"40.000000":0,"50.000000":0,"60.000000":0,"70.000000":0,"80.000000":0,"90.000000":0,"95.000000":0,"99.000000":0,"99.500000":0,"99.900000":0,"99.950000":0,"99.990000":0}},"total_ios":0},"job_runtime":3097,"usr_cpu":0.226025,"sys_cpu":98.12722,"ctx":646,"majf":0,"minf":26,"iodepth_level":{"1":0.1,"2":0.190557,"4":0.381114,"8":0.762227,"16":1.524455,"32":97.046369,">=64":0},"iodepth_submit":{"0":0,"4":100,"8":0,"16":0,"32":0,"64":0,">=64":0},"iodepth_complete":{"0":0,"4":99.901918,"8":0,"16":0,"32":0.1,"64":0,">=64":0},"latency_ns":{"2":0,"4":0,"10":0,"20":0,"50":0,"100":0,"250":0,"500":0,"750":0,"1000":0},"latency_us":{"2":0,"4":0,"10":0,"20":0,"50":0.070136,"100":0.124391,"250":0.485655,"500":0.838979,"750":1.765297,"1000":7.214694},"latency_ms":{"2":87.922136,"4":0.862799,"10":0.715911,"20":0,"50":0,"100":0,"250":0,"500":0,"750":0,"1000":0,"2000":0,">=2000":0},"latency_depth":32,"latency_target":0,"latency_percentile":100,"latency_window":0}],"disk_util":[{"name":"sda","read_ios":29339,"write_ios":43663,"read_merges":0,"write_merges":0,"read_ticks":3286,"write_ticks":4671,"in_queue":7957,"util":93.513166}]}')}},[[343,1,2]]]);
//# sourceMappingURL=main.32b3660f.chunk.js.map
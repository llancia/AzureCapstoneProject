<p align="center">
<svg height="30" viewBox="0 0 180 30" width="180"><g fill="none" fill-rule="evenodd"><path d="M57.6 17.239187c0 2.546698-2.085517 4.407747-4.965517 4.407747-2.88 0-4.965517-1.86105-4.965517-4.407747V7.835994H45.68276v9.501143c0 3.330298 2.88 6.170846 6.951723 6.170846 4.071724 0 6.951724-2.938498 6.951724-6.170846V7.835994H57.6v9.403193zm16.286897-9.403193h-5.36276v15.67199h5.36276c4.468965 0 7.547586-3.03645 7.547586-7.835996 0-4.701596-3.07862-7.835994-7.547586-7.835994zm-.19862 13.71299h-3.177932V9.794994h3.17793c3.376553 0 5.76 2.252847 5.76 5.876994 0 3.917998-2.482757 5.779046-5.76 5.876996zm43.49793.29385c-3.575172 0-5.95862-2.644648-5.95862-6.170846 0-3.526197 2.482758-6.072895 5.95862-6.072895 2.78069 0 4.468966 1.5672 4.468966 1.5672l.794483-1.3713s-1.787587-1.86105-5.46207-1.86105c-4.766896 0-7.746206 3.526198-7.746206 7.738045 0 4.309797 3.07862 7.933945 7.944827 7.933945 3.773793 0 5.66069-2.5467 5.66069-2.5467l-1.092414-1.175398c-.09931-.09795-1.588965 1.959-4.568276 1.959zm14.896553-14.00684h1.986206v15.67199h-1.986207zm10.924137 1.959h4.965517v13.71299h1.986207V9.794994h4.96552v-1.959H143.0069m30.587583 0l-4.766896 7.150344-4.866207-7.150347h-2.085518l5.95862 8.717546v6.954445h1.986208v-6.954444l5.85931-8.71754m-81.434482 0l-6.157242 15.67199h1.986207l1.688276-4.5057 6.45517-1.3713 2.18483 5.876998h1.986203l-6.05793-15.67199h-2.085518zm-1.886897 9.305242l2.97931-7.248294h.099315L97.92 16.063788l-5.56138 1.07745z" fill="currentColor"></path><path d="M29 .5l1 .5v13c0 5.551887-2.8897 8.695692-5.995216 10.099885L24.0094 24.1l-7.620963 4.388562c-.05877.03456-.11776.068527-.176957.101902l-.08642.049764.001806-.00254C14.48289 29.545895 12.684682 30 11 30 6 30 0 26 0 18V6l2 1v11c0 8 6 10 9 10 1.858706 0 4.86901-.76773 6.89043-3.254517C14.181726 23.872636 10 20.678703 10 14V2.2L2 7 0 6l10-6 1 .5 1 .5v13c0 6.939958 4.515283 8.612086 7.017542 8.933368C19.625786 21.62159 20 19.997902 20 18V5l2 1v12c0 1.852645-.321777 3.49077-.878395 4.91438C23.648223 22.549217 28 20.813144 28 14V2.25L22 6l-2-1 8-5 1 .5z" fill="#02B3E4"></path></g></svg>
  <h1 align="center">Azure Machine Learning Engineer | Capstone Project</h1>
    <p align="center">
    project_description
    <br/>
</p>

A company is sponsorizing some courses for data scientist and wanto to hire potential candidates. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training. Using information related to demographics, education, experience are in hands from candidates signup and enrollment we want to predict their propensity to a job change.


## Project Overview
We want to provide a machine learning solution to itentify those candidates willing to change their job and to do so, we want to provide a REST endopint serving a model which answer the question.

To train and deploy such model we follow the diagram



<svg id="graph-div" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="822.91748046875" style="max-width: 423.640625px;" viewBox="0 0 423.640625 822.91748046875"><style>#graph-div {font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}#graph-div .error-icon{fill:#552222;}#graph-div .error-text{fill:#552222;stroke:#552222;}#graph-div .edge-thickness-normal{stroke-width:2px;}#graph-div .edge-thickness-thick{stroke-width:3.5px;}#graph-div .edge-pattern-solid{stroke-dasharray:0;}#graph-div .edge-pattern-dashed{stroke-dasharray:3;}#graph-div .edge-pattern-dotted{stroke-dasharray:2;}#graph-div .marker{fill:#333333;stroke:#333333;}#graph-div .marker.cross{stroke:#333333;}#graph-div svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#graph-div .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#graph-div .cluster-label text{fill:#333;}#graph-div .cluster-label span{color:#333;}#graph-div .label text,#graph-div span{fill:#333;color:#333;}#graph-div .node rect,#graph-div .node circle,#graph-div .node ellipse,#graph-div .node polygon,#graph-div .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#graph-div .node .label{text-align:center;}#graph-div .node.clickable{cursor:pointer;}#graph-div .arrowheadPath{fill:#333333;}#graph-div .edgePath .path{stroke:#333333;stroke-width:2.0px;}#graph-div .flowchart-link{stroke:#333333;fill:none;}#graph-div .edgeLabel{background-color:#e8e8e8;text-align:center;}#graph-div .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#graph-div .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#graph-div .cluster text{fill:#333;}#graph-div .cluster span{color:#333;}#graph-div div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#graph-div :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><g class="output"><g class="clusters"></g><g class="edgePaths"><g class="edgePath LS-A LE-B" id="L-A-B" style="opacity: 1;"><path class="path" d="M213.44921875,80.01119995117188L213.44921875,86.17786661783855C213.44921875,92.3445332845052,213.44921875,104.67786661783855,213.44921875,117.01119995117188C213.44921875,129.34453328450522,213.44921875,141.67786661783853,213.44921875,147.84453328450522L213.44921875,154.01119995117188" marker-end="url(#arrowhead50)" style="fill:none"></path><defs><marker id="arrowhead50" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-B LE-C" id="L-B-C" style="opacity: 1;"><path class="path" d="M213.44921875,198.01119995117188L213.44921875,202.17786661783853C213.44921875,206.34453328450522,213.44921875,214.67786661783853,213.44921875,223.01119995117188C213.44921875,231.34453328450522,213.44921875,239.67786661783853,213.44921875,248.01119995117188C213.44921875,256.3445332845052,213.44921875,264.67786661783856,213.53255208333334,273.0945332845052C213.61588541666666,281.5111999511719,213.78255208333334,290.0111999511719,213.86588541666666,294.2611999511719L213.94921875,298.5111999511719" marker-end="url(#arrowhead51)" style="fill:none"></path><defs><marker id="arrowhead51" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-C LE-TR" id="L-C-TR" style="opacity: 1;"><path class="path" d="M179.64370013297872,342.5111999511719L173.0631094858156,346.5945332845052C166.48251883865248,350.67786661783856,153.32133754432624,358.8445332845052,146.74074689716312,367.0945332845052C140.16015625,375.3445332845052,140.16015625,383.67786661783856,140.16015625,387.8445332845052L140.16015625,392.0111999511719" marker-end="url(#arrowhead52)" style="fill:none"></path><defs><marker id="arrowhead52" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-C LE-TS" id="L-C-TS" style="opacity: 1;"><path class="path" d="M283.3227227393617,342.5111999511719L296.3783106161348,346.5945332845052C309.4338984929078,350.67786661783856,335.5450742464539,358.8445332845052,348.600662123227,370.7611999511719C361.65625,382.67786661783856,361.65625,398.3445332845052,361.65625,414.0111999511719C361.65625,429.67786661783856,361.65625,445.3445332845052,361.65625,457.3445332845052C361.65625,469.3445332845052,361.65625,477.67786661783856,361.65625,481.8445332845052L361.65625,486.0111999511719" marker-end="url(#arrowhead53)" style="fill:none"></path><defs><marker id="arrowhead53" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-TR LE-H" id="L-TR-H" style="opacity: 1;"><path class="path" d="M105.09217087765958,436.0111999511719L98.45050698138299,440.17786661783856C91.80884308510639,444.3445332845052,78.5255152925532,452.67786661783856,71.96718472960993,461.0945332845052C65.40885416666667,469.5111999511719,65.57552083333333,478.0111999511719,65.65885416666667,482.2611999511719L65.7421875,486.5111999511719" marker-end="url(#arrowhead54)" style="fill:none"></path><defs><marker id="arrowhead54" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-TR LE-AML" id="L-TR-AML" style="opacity: 1;"><path class="path" d="M175.22814162234042,436.0111999511719L181.86980551861703,440.17786661783856C188.51146941489364,444.3445332845052,201.7947972074468,452.67786661783856,208.51979443705673,461.0945332845052C215.24479166666666,469.5111999511719,215.41145833333334,478.0111999511719,215.49479166666666,482.2611999511719L215.578125,486.5111999511719" marker-end="url(#arrowhead55)" style="fill:none"></path><defs><marker id="arrowhead55" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-H LE-BM" id="L-H-BM" style="opacity: 1;"><path class="path" d="M65.7421875,530.5111999511719L65.65885416666667,536.5945332845052C65.57552083333333,542.6778666178385,65.40885416666667,554.8445332845052,67.06399644168123,567.3625154218483C68.71913871669578,579.8804975591914,72.19608993339158,592.7497951672109,73.93456554173946,599.1844439712207L75.67304115008736,605.6190927752305" marker-end="url(#arrowhead56)" style="fill:none"></path><defs><marker id="arrowhead56" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-TS LE-BM" id="L-TS-BM" style="opacity: 1;"><path class="path" d="M314.79992055084745,530.0111999511719L301.6659494173729,536.1778666178385C288.5319782838983,542.3445332845052,262.26403601694915,554.6778666178385,231.17510782497615,570.9546965010193C200.0861796330031,587.2315263842,164.17626551600623,607.4518528172282,146.22130845750777,617.5620160337422L128.26635139900932,627.6721792502564" marker-end="url(#arrowhead57)" style="fill:none"></path><defs><marker id="arrowhead57" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-BM LE-EP" id="L-BM-EP" style="opacity: 1;"><path class="path" d="M87.7890625,696.9174499511719L87.7890625,703.0841166178385C87.7890625,709.2507832845052,87.7890625,721.5841166178385,101.7040502852448,734.328359797349C115.61903807048958,747.0726029768593,143.44901364097916,760.2277560025468,157.36400142622395,766.8053325153907L171.27898921146874,773.3829090282344" marker-end="url(#arrowhead58)" style="fill:none"></path><defs><marker id="arrowhead58" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath LS-TS LE-EP" id="L-TS-EP" style="opacity: 1;"><path class="path" d="M370.0635593220339,530.0111999511719L372.4201536016949,536.1778666178385C374.7767478813559,542.3445332845052,379.4899364406779,554.6778666178385,381.846530720339,574.7533874511719C384.203125,594.8289082845052,384.203125,622.6466166178385,384.203125,650.4643249511719C384.203125,678.2820332845052,384.203125,706.0997416178385,363.3151318389537,727.3380782124126C342.4271386779073,748.5764148069865,300.65115235581453,763.2353796628009,279.7631591947682,770.5648620907083L258.8751660337218,777.8943445186155" marker-end="url(#arrowhead59)" style="fill:none;stroke-width:2px;stroke-dasharray:3;"></path><defs><marker id="arrowhead59" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(213.44921875,117.01119995117188)" style="opacity: 1;"><g transform="translate(-74.1796875,-12)" class="label"><rect rx="0" ry="0" width="148.359375" height="24"></rect><foreignObject width="148.359375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-A-B" class="edgeLabel L-LS-A' L-LE-B">Download &amp; Register</span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-B-C" class="edgeLabel L-LS-B' L-LE-C"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-C-TR" class="edgeLabel L-LS-C' L-LE-TR"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-C-TS" class="edgeLabel L-LS-C' L-LE-TS"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-TR-H" class="edgeLabel L-LS-TR' L-LE-H"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-TR-AML" class="edgeLabel L-LS-TR' L-LE-AML"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><rect rx="0" ry="0" width="0" height="0"></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-H-BM" class="edgeLabel L-LS-H' L-LE-BM"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(235.99609375,567.0111999511719)" style="opacity: 1;"><g transform="translate(-25.09375,-12)" class="label"><rect rx="0" ry="0" width="50.1875" height="24"></rect><foreignObject width="50.1875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-TS-BM" class="edgeLabel L-LS-TS' L-LE-BM">Testing</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(87.7890625,733.9174499511719)" style="opacity: 1;"><g transform="translate(-24.328125,-12)" class="label"><rect rx="0" ry="0" width="48.65625" height="24"></rect><foreignObject width="48.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-BM-EP" class="edgeLabel L-LS-BM' L-LE-EP">Deploy</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(384.203125,650.4643249511719)" style="opacity: 1;"><g transform="translate(-17.4375,-12)" class="label"><rect rx="0" ry="0" width="34.875" height="24"></rect><foreignObject width="34.875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span id="L-L-TS-EP" class="edgeLabel L-LS-TS' L-LE-EP">REST</span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-20" label-offset-y="9.337066332524081" transform="translate(213.44921875,44.00559997558594)" style="opacity: 1;"><path d="M 0,9.337066332524081 a 37.2578125,9.337066332524081 0,0,0 74.515625 0 a 37.2578125,9.337066332524081 0,0,0 -74.515625 0 l 0,53.33706633252408 a 37.2578125,9.337066332524081 0,0,0 74.515625 0 l 0,-53.33706633252408" transform="translate(-37.2578125,-36.005599498786125)" class="label-container"></path><g class="label" transform="translate(0,0)"><g transform="translate(-27.2578125,-12)"><foreignObject width="54.515625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Dataset</div></foreignObject></g></g></g><g class="node default" id="flowchart-B-21" transform="translate(213.44921875,176.01119995117188)" style="opacity: 1;"><rect rx="5" ry="5" x="-68.0625" y="-22" width="136.125" height="44" class="label-container"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-58.0625,-12)"><foreignObject width="116.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">AzureMl Dataset</div></foreignObject></g></g></g><g class="node default" id="flowchart-C-23" transform="translate(213.44921875,320.0111999511719)" style="opacity: 1;"><polygon points="0,0 203.03125,0 203.03125,-44 0,-44 0,0 -8,0 211.03125,0 211.03125,-44 -8,-44 -8,0" transform="translate(-101.515625,22)" class="label-container"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-91.515625,-12)"><foreignObject width="183.03125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Data Preparation Pipeline</div></foreignObject></g></g></g><g class="node default" id="flowchart-TR-25" transform="translate(140.16015625,414.0111999511719)" style="opacity: 1;"><rect rx="5" ry="5" x="-57.296875" y="-22" width="114.59375" height="44" class="label-container"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-47.296875,-12)"><foreignObject width="94.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Training Data</div></foreignObject></g></g></g><g class="node default" id="flowchart-TS-27" transform="translate(361.65625,508.0111999511719)" style="opacity: 1;"><rect rx="5" ry="5" x="-53.984375" y="-22" width="107.96875" height="44" class="label-container"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-43.984375,-12)"><foreignObject width="87.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Testing Data</div></foreignObject></g></g></g><g class="node default" id="flowchart-H-29" transform="translate(65.2421875,508.0111999511719)" style="opacity: 1;"><polygon points="0,0 98.484375,0 98.484375,-44 0,-44 0,0 -8,0 106.484375,0 106.484375,-44 -8,-44 -8,0" transform="translate(-49.2421875,22)" class="label-container"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-39.2421875,-12)"><foreignObject width="78.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Hyperdrive</div></foreignObject></g></g></g><g class="node default" id="flowchart-AML-31" transform="translate(215.078125,508.0111999511719)" style="opacity: 1;"><polygon points="0,0 69.1875,0 69.1875,-44 0,-44 0,0 -8,0 77.1875,0 77.1875,-44 -8,-44 -8,0" transform="translate(-34.59375,22)" class="label-container"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-24.59375,-12)"><foreignObject width="49.1875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">AutoMl</div></foreignObject></g></g></g><g class="node default" id="flowchart-BM-33" transform="translate(87.7890625,650.4643249511719)" style="opacity: 1;"><circle x="-46.453125" y="-22" r="46.453125" class="label-container"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-36.453125,-12)"><foreignObject width="72.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">BestModel</div></foreignObject></g></g></g><g class="node default" id="flowchart-EP-37" transform="translate(213.44921875,792.9174499511719)" style="opacity: 1;"><polygon points="11,0 94.375,0 105.375,-22 94.375,-44 11,-44 0,-22" transform="translate(-52.6875,22)" class="label-container"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-31.6875,-12)"><foreignObject width="63.375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Endpoint</div></foreignObject></g></g></g></g></g></g></svg>

Using the data gathered from Kaggle we registered them a dataset in an azureml workspace. Then we raun the **setup** pipeline which produces the training and the test dataset. 

On the train dataset we lanch both an *AutoMl* and an *Hyperdrive* Model to find the best possible model wrt the ROC-AUC classification metric.

The best model is then served as an endpoint to allow inference operations.
## Project Set Up and Installation
From the raw data available [here](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists) i've set up a pipeline that prepare the data for either the hyper-parameters search and for automl task.
It also take care of train and test splitting.

Details are available in the notebook `notebooks/create_dataset.ipynb`

### Get the data into your Azure ML Studio

Before running the SetUp Pipeline we need to get the original dataset inside the Azure ML workspace.

To do that i've create a script available in `scripts\download_dataset.sh` which downloads the file inside the data folder and then we can use the python script `scripts\create_dataset.py` to register it as an Azure Ml Dataset.


## Dataset
The original dataset contains:
- enrollee_id : Unique ID for candidate
- city: City code
- city_ development _index : Developement index of the city (scaled)
- gender: Gender of candidate
- relevent_experience: Relevant experience of candidate
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of candidate
- major_discipline :Education major discipline of candidate
- experience: Candidate total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed
- target: 0 – Not looking for job change, 1 – Looking for a job change


Note:

- The dataset is imbalanced.
- Most features are categorical (Nominal, Ordinal, Binary), some with high - cardinality.
- Missing imputation can be a part of your pipeline as well.
 about the data you are using and where you got it from.

### Task
We have to predict which data scientist is looking for a job change and thus, is a better prospect in terms of hiring.

### Access

By running the SetUp Pipeline, from the original dataset we register two different datasets

![](img/1.PNG)

- `HRAnalytics_train_dataset`
- `HRAnalytics_test_dataset`

![](img\2.PNG)

we can then access using the following python code: 

```{python}
# Dataset
dataset_name = "HRAnalytics_train_dataset"

dataset = ws.datasets[dataset_name]

df = dataset.to_pandas_dataframe()
df.head()
```


## Automated ML

In this first step, an AutoML run was lunched to search for a best possible model to handle the predictive task.

An `AutoMLConfig` is the the object we need to instantiate to configuring the experiment run:

```{python}

automl_settings = {
    "experiment_timeout_minutes": 20,
    "max_concurrent_iterations": 4,
    "n_cross_validations": 4,
    "primary_metric" : 'AUC_weighted'
}

automl_config = AutoMLConfig(compute_target=compute_cluster,
                             task="classification",
                             label_column_name="target",   
                             training_data =dataset,
                             enable_early_stopping=True,
                             featurization='auto',
                             debug_log="automl_errors.log",
                             **automl_settings
                            )
```

The parameters are:

- **experiment_timeout_minutes**: maximum amount of time in minutes that all iterations combined can take before the experiment terminates. It has been set to 20

- **max_concurrent_iterations**: maximum number of iterations that would be executed in parallel. It has been set to 4

- **n_cross_validations**: how many cross validations to perform when user validation data is not specified. It has been set to 4

- **primary_metric**: the metric that Automated Machine Learning will optimize for model selection. It has been set to AUC weighted between classes


### Results
After submitting the run to the Compute cluster we wait for it to complete by monitoring the widget: 

![](img/3.PNG)

After it's done we can get the result of the AutoML job by gathering the:

* best run
* the best model
* the metrics associate to the best model
using the following code
```

best_run_automl, best_model_automl = remote_run.get_output()
best_run_metrics_automl = best_run_automl.get_metrics()

```

We fetched the model and tested it against the `test_dataset` we held for the purpose:

```
y_true = test_df["target"]
x = test_df.drop(columns=["target"])

y_pred= best_model_automl.predict(x)
```

The best model is a Voting Ensamble achieving a AUC weighted of 0.80, we can see the detail of the models here
```
PipelineWithYTransformations(Pipeline={'memory': None,
                                       'steps': [('datatransformer',
                                                  DataTransformer(enable_dnn=False, enable_feature_sweeping=True, feature_sweeping_config={}, feature_sweeping_timeout=86400, featurization_config=None, force_text_dnn=False, is_cross_validation=True, is_onnx_compatible=False, observer=None, task='classification', working_dir='/mn...
)), ('extratreesclassifier', ExtraTreesClassifier(bootstrap=False, ccp_alpha=0.0, class_weight='balanced', criterion='gini', max_depth=None, max_features=None, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=0.01, min_samples_split=0.056842105263157895, min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=1, oob_score=False, random_state=None, verbose=0, warm_start=False))], verbose=False))], flatten_transform=None, weights=[0.06666666666666667, 0.3333333333333333, 0.06666666666666667, 0.13333333333333333, 0.06666666666666667, 0.13333333333333333, 0.13333333333333333, 0.06666666666666667]))],
                                       'verbose': False},
                             y_transformer={},
                             y_transformer_name='LabelEncoder')
                             
```
and we can take a look at the run building it by looking at the studio: 
![](img/4.PNG)

The detail of the best run are show here, describing the mertrics and the run details
![](img/automl.png)

while the model is available from the Model tab

![](img/automl2.png)

## Hyperparameter Tuning

In this task, an HyperDrive run  using a customized model is built.

The model chosen is a RandomForest with its scikit-learn implementation.

RandomForest is a classification algorithm using a bagging of different trees. It has a very good resistance to overfitting and quite a lot of different hyperparameters to tune.

To ensure the different data are ready to be handeled by the classifier an sklearn pipeline is built around it as stated in the `train.py` script. 

**The script is available in** `notebooks\steps_scripts\model\train.py`


```
    numeric_features = ['city_development_index', 'training_hours']

    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    categorical_features = ['city',  'gender', 'relevent_experience',
        'enrolled_university', 'education_level', 'major_discipline',
        'experience', 'company_size', 'company_type', 'last_new_job']

    categorical_transformer = Pipeline(steps=[
        ('caster', StringCaster()),
        ('encoder', OneHotEncoder(handle_unknown='ignore')),
        ]
    )


    preprocessor = ColumnTransformer(
        transformers=[ 
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])


    clf = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', RandomForestClassifier(**classifier_params))])

```

The script can be lunched by passing different parameters representing some of  the hyperparameters of the model: 

```
    parser.add_argument('--n_estimators', type=int )
    parser.add_argument('--max_features', type=str)
    parser.add_argument('--max_depth', type=int)
```

* **n_estimator** is the number of the tree composing the ensamble
* **max_features** The number of features to consider when looking for the best split
* **max_depth** The maximum depth of the tree. I

We went through the combination of parameters to search the best one via a Random search which it does not give the absolute best parameters but its usually pretty close and helps in reducing the iteratons w.r.t a Grid Search approach.

To do this we defined a parameter space

```{python}
ps = RandomParameterSampling({
        "--n_estimators": choice( [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]),
        "--max_features": choice('auto', 'sqrt'),
        "--max_depth": choice([int(x) for x in np.linspace(10, 110, num = 11)])
    }
)
```
and a early termination policy
```
policy = BanditPolicy(slack_factor = 0.1,
                        evaluation_interval = 1,
                        delay_evaluation = 5)
```

to finally submit a Hyperdrive run

```
hyperdrive_config = HyperDriveConfig(run_config=src,
                                     hyperparameter_sampling=ps,
                                     policy = policy,
                                     primary_metric_name="AUC",
                                     primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
                                     max_total_runs=20,
                                     max_concurrent_runs=4,
                                     )
```

and use the widget to monitor it and look at the evolution of the best metric as the job explore the parameters space.

![](img/5.PNG)
### Results
We collected the best run by AUC
```
best_run = remote_run.get_best_run_by_primary_metric()
```
and we take a look at the best run and its detail from the azureml studio interface.


![](img/6.PNG)

we can deep dive into the best run which show as the best set of hyper-parameters and the recieved accuracy.
![](img/7.PNG)

this run achieved a score of 0.8 with the set of hyperparameters: 


```
hyperparameters : {"--max_depth": 20,
 "--max_features": "sqrt",
  "--n_estimators": 800}
```

and registered the best model by:

```
registered_model = best_run.register_model(model_name = experiment_name+"model", model_path= saved_model)
```

this saves the model and allow us to use it in other jobs, including a deployment operation. The models can be explored from the model section of azure ml studio.

This are the details, note that it links back to the run producing it allowing us to reproduce the experiment in case of need. 
![](img/8.PNG)
## Model Deployment

Performance of the two models obtained by automl and hyperdrive are pretty much comparable. 

I've decided to deploy the custom model obtained by hyperdrive to force myself to deploy a completely custom item. 

### Adapt environmet

First i need to add to the Python env used for training two dependencies used to handle the inference and the service.

```
conda.add_pip_package("azureml-model-management-sdk")
conda.add_pip_package("inference-schema")
env.python.conda_dependencies = conda
```

the final environment is available in `code\env`

then we create `AciWebservice` configurtion and we used it for deploy
```
from azureml.core.model import Model, InferenceConfig
from azureml.core.webservice import AciWebservice

inference_config = InferenceConfig(entry_script='score.py', environment=env, source_directory='./steps_scripts/model/' )


aci_deployment_config = AciWebservice.deploy_configuration(cpu_cores=1,
                                                           memory_gb=1,
                                                           auth_enabled=True,
                                                           enable_app_insights=True,
                                                           description='AutoML model deploy')
```

is important to refer to the `score.py` script which handles the calls to the rest endpoint.

Aside from deserializing the model and provide a `run(data)` function, i've added a set of sample input for him to infer the proper schema.



```

service_name = "test-deploy-ht"
service = Model.deploy(workspace=ws,
                       name=service_name,
                       models=[registered_model],
                       inference_config=inference_config,
                       deployment_config=aci_deployment_config,
                       overwrite=True
                      )
service.wait_for_deployment(show_output=True)


print('Deployment state: ', service.state)
print('Scoring URI: ', service.scoring_uri)
```

This is how the endpoint appears after the deploy, the status is healthy and it signals us that we can now call.
![](img/9.PNG)

we wait for deployment till we can make request to the endpoint by using the code in `endpoint.py`

```{python}
import requests
import json
from numpy import nan 
# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://96f9e630-43b1-4876-820e-9b1d857c7bb2.westeurope.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '4vxJev904dUJTZGIEpsexvGl55AUcBDC'
# A set of data to score, so we get one results back
data = {"data":
        [{'city': 'city_103',
  'city_development_index': 0.92,
  'gender': nan,
  'relevent_experience': 'Has relevent experience',
  'enrolled_university': 'no_enrollment',
  'education_level': 'Graduate',
  'major_discipline': 'STEM',
  'experience': '>20',
  'company_size': '10/49',
  'company_type': 'Pvt Ltd',
  'last_new_job': '>4',
  'training_hours': 140}]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)
# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'
# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
```

The service can handle also multiple inference with a single request

```
multiple_run = x.sample(78).to_dict(orient="records")
input_data = json.dumps({"data": multiple_run})
#print(input_data)
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
```
producing a list of results

```
{"result": ["no", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no"]}

```

finally we printed the logs and deleted the service.

```
print(service.get_logs())
service.delete()
```

## Screen Recording
link to screen cast https://youtu.be/PnpwXfrYE0w
containing 
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Future improvements

* **Single pipeline from dataset to deploy** the pipeline used in the setup phase may be further extended to cover all the training steps, testing against held out test data and then deploy of the best model.

* **Model explaination with shap values** Is interesting to compute some explainition of the model (eg using shapely values). The contribution of each feature may be returned from the service during rest call.

* **Pipeline for batch inferencing** Scoring of the model against a new dataset should be done offline with a batch inferencing pipeline. 
import { useState } from "react";
import axios from "axios";


function App(){


const [match,setMatch]=useState("");

const [result,setResult]=useState("");



async function analyze(){


const response =
await axios.post(
"http://localhost:8000/analyze",
{
description:match
}
);


setResult(
response.data.analysis
);


}



return (

<div style={{
padding:"40px",
fontFamily:"Arial"
}}>


<h1>
⚽ Soccer AI Explainer
</h1>


<p>
AI-powered soccer tactical analysis assistant
</p>


<textarea

rows="8"

cols="60"

placeholder="Describe a soccer match situation..."

value={match}

onChange={
(e)=>setMatch(e.target.value)
}

/>



<br/>


<button onClick={analyze}>

Analyze

</button>



<h2>
Analysis Result
</h2>


<pre>

{result}

</pre>


</div>

);


}


export default App;

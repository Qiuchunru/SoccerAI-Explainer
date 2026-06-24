
import { useState } from "react";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const analyze = async () => {
    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    setResult(data.analysis);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Soccer AI Explainer</h1>

      <textarea
        rows={10}
        cols={60}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter soccer match description..."
      />

      <br /><br />

      <button onClick={analyze}>
        Analyze
      </button>

      <h2>Result</h2>
      <pre>{result}</pre>
    </div>
  );
}

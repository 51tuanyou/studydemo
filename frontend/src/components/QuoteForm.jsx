import { useState } from "react";
import { getQuote } from "../api/quoteApi";

export default function QuoteForm() {
  const [emailText, setEmailText] = useState("");
  const [quotes, setQuotes] = useState({});

  const handleSubmit = async () => {
    const res = await getQuote(emailText);
    setQuotes(res);
  };

  return (
    <div>
      <textarea
        rows={10}
        cols={50}
        placeholder="Paste email content here"
        value={emailText}
        onChange={(e) => setEmailText(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit}>Get Quote</button>
      <div>
        {Object.entries(quotes).map(([name, price]) => (
          <div key={name}>
            {name}: {price}
          </div>
        ))}
      </div>
    </div>
  );
}

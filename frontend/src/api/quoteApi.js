export async function getQuote(emailText) {
  const res = await fetch("http://127.0.0.1:8000/api/quote/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email_text: emailText }),
  });
  return res.json();
}

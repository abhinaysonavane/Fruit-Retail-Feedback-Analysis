const form=document.getElementById('feedbackForm');const resultDiv=document.getElementById('result');
form.addEventListener('submit',async e=>{e.preventDefault();const payload={FeedbackText:document.getElementById('feedback').value,
Freshness:document.getElementById('freshness').value,Price:document.getElementById('price').value,
Quality:document.getElementById('quality').value,Service:document.getElementById('service').value};
resultDiv.innerText='Predicting...';try{const res=await fetch('/predict',{method:'POST',headers:{'Content-Type':'application/json'},
body:JSON.stringify(payload)});const data=await res.json();if(res.ok){resultDiv.innerHTML='<b>Prediction:</b> '+data.prediction;}
else{resultDiv.innerText=data.error||'Error';}}catch(err){resultDiv.innerText='Request failed: '+err.message;}});
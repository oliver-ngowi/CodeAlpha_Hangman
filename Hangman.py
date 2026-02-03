from pathlib import Path
import webbrowser

HTML = r'''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Hangman</title>
  <style>
    :root{--bg:#eaf8ff;--card:#ffffff;--accent:#bfe9ff;--text:#0b3a57}
    *{box-sizing:border-box}
    body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:var(--bg);color:var(--text);display:flex;align-items:center;justify-content:center;height:100vh}
    .wrap{background:linear-gradient(180deg,var(--card),#f8fdff);padding:28px;border-radius:12px;box-shadow:0 8px 30px rgba(11,58,87,0.08);width:420px;max-width:95%}
    h1{margin:0 0 8px;font-size:20px;text-align:center}
    .status{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
    .word{letter-spacing:8px;font-size:28px;text-align:center;margin:18px 0;font-weight:600}
    .keyboard{display:grid;grid-template-columns:repeat(9,1fr);gap:6px}
    button.letter{padding:10px;border-radius:6px;background:var(--accent);border:1px solid rgba(11,58,87,0.08);cursor:pointer;font-weight:600}
    button.letter:disabled{opacity:0.45;cursor:default}
    .meta{font-size:14px}
    .controls{display:flex;justify-content:space-between;margin-top:14px}
    .btn{background:var(--text);color:white;padding:8px 12px;border-radius:8px;border:none;cursor:pointer}
    .hangman-wrap{display:flex;justify-content:center;margin:6px 0}
    .part{display:none}
    /* hint removed */
    .message{margin-top:10px;text-align:center;font-weight:700}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Hangman</h1>
    <div class="status">
      <div class="meta">Attempts left: <span id="attempts">6</span></div>
    </div>
    <div class="hangman-wrap">
      <svg id="hangman" width="200" height="240" viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <!-- Gallows (always visible) -->
        <line x1="20" y1="220" x2="180" y2="220" stroke="#0b3a57" stroke-width="6" />
        <line x1="50" y1="220" x2="50" y2="20" stroke="#0b3a57" stroke-width="6" />
        <line x1="50" y1="20" x2="130" y2="20" stroke="#0b3a57" stroke-width="6" />
        <line x1="130" y1="20" x2="130" y2="44" stroke="#0b3a57" stroke-width="6" />

        <!-- Parts: head, body, left arm, right arm, left leg, right leg -->
        <circle id="part-1" class="part" cx="130" cy="64" r="18" fill="none" stroke="#0b3a57" stroke-width="4" />
        <line id="part-2" class="part" x1="130" y1="82" x2="130" y2="140" stroke="#0b3a57" stroke-width="4" />
        <line id="part-3" class="part" x1="130" y1="96" x2="106" y2="120" stroke="#0b3a57" stroke-width="4" />
        <line id="part-4" class="part" x1="130" y1="96" x2="154" y2="120" stroke="#0b3a57" stroke-width="4" />
        <line id="part-5" class="part" x1="130" y1="140" x2="110" y2="184" stroke="#0b3a57" stroke-width="4" />
        <line id="part-6" class="part" x1="130" y1="140" x2="150" y2="184" stroke="#0b3a57" stroke-width="4" />
      </svg>
    </div>
    <div class="word" id="word">_ _ _ _ _</div>
    <div class="keyboard" id="keyboard"></div>
    <div class="controls">
      <button class="btn" id="reset">Reset</button>
      <div class="meta">Guessed: <span id="guessed">-</span></div>
    </div>
    <div class="message" id="message"></div>
  </div>

  <script>
    const words = ["WEATHER","GRAPES","COMPUTER","STUDENT","FOOTBALL"];
    let secret = '';
    let attempts = 6;
    let guessed = new Set();

    const elAttempts = document.getElementById('attempts');
    const elWord = document.getElementById('word');
    const elKeyboard = document.getElementById('keyboard');
    const elGuessed = document.getElementById('guessed');
    const elMessage = document.getElementById('message');
    const hangmanParts = [...document.querySelectorAll('.part')];

    function pick(){ secret = words[Math.floor(Math.random()*words.length)]; attempts=6; guessed.clear(); render(); }

    function render(){
      elAttempts.textContent = attempts;
      const display = [...secret].map(ch => guessed.has(ch) ? ch : '_').join(' ');
      elWord.textContent = display;
      elGuessed.textContent = [...guessed].join(', ') || '-';
      elMessage.textContent = '';
      updateHangman();
      if(!display.includes('_')){ elMessage.textContent = 'You Win! 🎉'; disableAll(); }
      if(attempts<=0){ elMessage.textContent = 'Game Over — Word: ' + secret; disableAll(); }
    }

    function updateHangman(){
      const wrongs = 6 - attempts;
      hangmanParts.forEach((p,i)=> p.style.display = i < wrongs ? 'block' : 'none');
    }

    function disableAll(){ document.querySelectorAll('.letter').forEach(b=>b.disabled=true); }

    function onLetter(letter, btn){ if(attempts<=0) return; if(guessed.has(letter)) return; guessed.add(letter); btn.disabled=true; if(!secret.includes(letter)){ attempts--; } render(); }

    function makeKeyboard(){
      const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
      elKeyboard.innerHTML='';
      letters.forEach(l=>{
        const b = document.createElement('button'); b.className='letter'; b.textContent=l; b.onclick = ()=> onLetter(l,b); elKeyboard.appendChild(b);
      });
    }

    document.getElementById('reset').addEventListener('click', ()=>{ pick(); makeKeyboard(); });

    // init
    makeKeyboard(); pick();
  </script>
</body>
</html>
'''

def write_ui():
    out = Path(__file__).with_name('hangman_ui.html')
    out.write_text(HTML, encoding='utf-8')
    print(f'Wrote UI to {out}')
    webbrowser.open(out.as_uri())

if __name__ == '__main__':
    write_ui()

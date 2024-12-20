
deltaX = 50;

function playGame() {
  const player = document.getElementById("player");
  console.log(player.getBoundingClientRect());
  for (let i = 0; i <= 10; i++) {
    // console.log(player);
    // player.style.right += 20;
    requestAnimationFrame(movePlayer);
    console.log(player.getBoundingClientRect());
    deltaX += 40;
  }
  return 2;
}

function movePlayer() {
  const player = document.getElementById("player");
  player.style.transform = `translate(${deltaX}px, 0px)`;
  // requestAnimationFrame(movePlayer);
}

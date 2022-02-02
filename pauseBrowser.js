window.addEventListener('keydown', function(event) { 
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }
  let handled = false;
  if (event.keyCode == 123) {
    handled = true;
    debugger;  // 123 is the keyCode of F12
  }
  if (handled) {
    // Suppress "double action" if event handled
    event.preventDefault();
  }
});
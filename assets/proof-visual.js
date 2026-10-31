/* Proof Physical Therapy — shared front-end for visual components.
   Click-to-load map: no third-party (Google Maps) request until the visitor opts in. */
(function () {
  var btn = document.getElementById('maploadbtn');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var facade = document.getElementById('mapfacade');
    if (!facade) return;
    var q = btn.getAttribute('data-q') || '44056 Mound Rd Suite 103, Sterling Heights, MI 48314';
    var ifr = document.createElement('iframe');
    ifr.src = 'https://www.google.com/maps?q=' + encodeURIComponent(q) + '&output=embed';
    ifr.title = 'Map of Proof Physical Therapy, ' + q;
    ifr.loading = 'lazy';
    ifr.referrerPolicy = 'no-referrer-when-downgrade';
    facade.replaceWith(ifr);
  });
})();

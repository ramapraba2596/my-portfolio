emailjs.init({
  publicKey: "uTXe-_R35nrkE7sVh",
});

const form = document.querySelector(".contact-form");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  emailjs.sendForm(
    "service_8qidlm1",
    "template_t7oxvwd",
    this
  ).then(() => {
    alert("Message sent successfully!");
    form.reset();
  }).catch((error) => {
    alert("Failed to send message.");
    console.log(error);
  });
});
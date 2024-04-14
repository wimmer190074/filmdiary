<template>
    <div>
      <div class="uk-position-relative">
        <div class="uk-position-top">
          <div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky;">
            <nav class="uk-navbar-container" uk-navbar>
              <div class="uk-container">
                <div uk-navbar>
                  <div class=".uk-navbar-center">
                    <ul class="uk-navbar-nav">
                        <button class="uk-button uk-button-default navsmallscreen" type="button" uk-toggle="target: #offcanvas-nav"><span uk-icon="icon: menu; ratio: 2"></span></button>
                        <!-- <li><router-link class="uk-logo" to="/"><img src="" width="100"/></router-link></li> -->
                        <li class="navbigscreen">
                          <router-link to="/">Home</router-link>
                        </li>
                        <li class="navbigscreen">
                          <router-link to="/watched">Watched Movies</router-link>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </nav>
            </div>
          </div>
        <div id="offcanvas-nav" uk-offcanvas="mode: push; overlay: true" class="navsmallscreen">
            <div class="uk-offcanvas-bar offcanvasstyle">
              <ul class="uk-nav uk-nav-primary uk-margin-auto-vertical">
                <li class="uk-active"><router-link to="/">Home</router-link></li>
                <li><router-link to="/watched">Watched</router-link></li>
              </ul>
            </div>
          </div>
    </div>
    <div style="height: 80px;"></div>
    </div>
</template>
  
<style>
.img-logo {
  height: auto !important;
}
.nbrounded {
  border-radius: 50px !important;
}

@media (max-width: 640px){
  .img-logo{
    height: 400px !important;
  }
}
@media (max-width: 1075px){
  .navbigscreen {
    display: none !important;
  }
}

@media (min-width: 1075px) {
  .navsmallscreen {
    display: none !important;
  }
}

</style>
<div class="page">
 
     <div>
   
        <header>
            <slot name="header">header</slot>
        </header>
  
        <article>
            <slot name="body">body</slot>
        </article>
   
    </div> <!-- End: Wrapper (Without footer) -->
 
 
     <footer>
        <slot name="footer">footer</slot>
    </footer>
 
</div>

<style>
    .page {
        min-height:calc(100vh-8px);
        display:flex;
        flex-direction:column; 
        justify-content:space-between;
    }
</style>
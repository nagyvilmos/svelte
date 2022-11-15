<script>
    import { afterUpdate } from 'svelte';	
      let self;
      export let width;
      export let height;
      export let chart={};
      
      afterUpdate(()=> {
          const ctx = self.getContext("2d");
          let {minX, minY, maxX, maxY} = chart
          ctx.lineWidth=1
          const scaleX = width/100.0;
          const scaleY = height/100.0;
          console.log({height,width, scaleX,scaleY})
  
          const toX = (x) => x*scaleX;
          const toY = (y) => y*scaleY;
          const rectangle = (x,y,w,h) => {
              ctx.strokeRect(toX(x), toY(y), w*scaleX, h*scaleY);
          }
          const line = (...points) => {
              points.forEach((p,i) => i==0
                                          ? ctx.moveTo(toX(p[0]), toY(p[1]))
                                          :ctx.lineTo(toX(p[0]), toY(p[1])))				
              ctx.stroke();
          }
          rectangle(0,0,100,100)
          //line([5,5], [50,90],[95,20])
          //line([0,100],[10,99],[20,96],[30,91],[40,84],[50,75],[60,64],[70,51],[80,36],[90,9],[100,0])
          line(...[...Array(101).keys()].map(x => [x,100-((x**2)/100)]))
          line(...[...Array(101).keys()].map(x => [x,((x**2)/100)]))
          line(...[...Array(101).keys()].map(x => [x,100-(((100-x)**2)/100)]))
          line(...[...Array(101).keys()].map(x => [x,(((100-x)**2)/100)]))
          /*ctx.strokeRect(0, 0, 100*scaleX, 100*scaleY);
          ctx.moveTo(15,7.5);
          ctx.lineTo(150,120);
          ctx.lineTo(280, 20);
          ctx.stroke();
          //ctx.scale(height/100,width/100);
          ctx.strokeRect(0, 0, 100, 100);
          ctx.moveTo(5,5);
          ctx.lineTo(50,90);
          ctx.lineTo(95, 20);
          ctx.stroke();
          */
      })
  </script>
  
  <canvas width={width} height={height} bind:this={self} /> 
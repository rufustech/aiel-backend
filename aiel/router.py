from rest_framework import routers
from team.views import TeamViewSet
from events.views import EventViewSet
from research.views import ResearchViewSet
from board.views import BoardViewSet
from community.views import CommunityViewSet
from briefs.views import BriefViewSet
from resources.views import ResourceViewSet
from mediaapi.views import MediaViewSet
from contactapi.views import ContactUsViewSet
from subscription.views import SubscriptionViewSet
from casestudy.views import CaseStudyViewSet
from legalcommentary.views import LegalCommentaryViewSet
from multimediaresource.views import MultimediaResourceViewSet
from newsletter.views import NewsLetterViewSet
from researchhighlight.views import ResearchHighlightViewSet
from guides.views import GuideViewSet
from photos.views import PhotoViewSet, PhotoGalleryViewSet
from podcasts.views import PodcastViewSet
from videos.views import VideoViewSet
from cms.views import ArticleViewSet, CategoryViewSet, CommentViewSet, LikeDislikeViewSet

router = routers.DefaultRouter()
router.register('team', TeamViewSet)
router.register('event', EventViewSet)
router.register('research', ResearchViewSet)
router.register('board', BoardViewSet)
router.register('community', CommunityViewSet)
router.register('brief', BriefViewSet)
router.register('resource', ResourceViewSet)
router.register('mediaapi', MediaViewSet)
router.register('contact', ContactUsViewSet)
router.register('subscription', SubscriptionViewSet)
router.register('casestudy', CaseStudyViewSet)
router.register('legalcommentary', LegalCommentaryViewSet)
router.register('multimediaresource', MultimediaResourceViewSet)
router.register('newsletter', NewsLetterViewSet)
router.register('researchhighlight', ResearchHighlightViewSet)
router.register('guide', GuideViewSet)
router.register('photo', PhotoViewSet)
router.register('photogallery', PhotoGalleryViewSet)
router.register('podcast', PodcastViewSet)
router.register('video', VideoViewSet)
router.register('cms/article', ArticleViewSet)
router.register('cms/category', CategoryViewSet)
router.register('cms/comment', CommentViewSet)
router.register('cms/likedislike', LikeDislikeViewSet)
